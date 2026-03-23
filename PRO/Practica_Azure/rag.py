# rag.py — Parte 1: setup
import os
import numpy as np
import faiss
import pickle
from dotenv import load_dotenv
from openai import AzureOpenAI
from azure.storage.blob import BlobServiceClient
load_dotenv()
client_chat = AzureOpenAI(
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    api_key=os.getenv('AZURE_OPENAI_KEY'),
    api_version=os.getenv('AZURE_OPENAI_API_VERSION')
)
client_embedding = AzureOpenAI(
    azure_endpoint=os.getenv('AZURE_OPENAI_EMBEDDING_ENDPOINT',
                             os.getenv('AZURE_OPENAI_ENDPOINT')),
    api_key=os.getenv('AZURE_OPENAI_EMBEDDING_KEY',
                      os.getenv('AZURE_OPENAI_KEY')),
    api_version=os.getenv('AZURE_OPENAI_API_VERSION')
)
CHAT_MODEL = os.getenv('AZURE_OPENAI_DEPLOYMENT')
EMBEDDING_MODEL = os.getenv('AZURE_OPENAI_EMBEDDING')
UMBRAL = float(os.getenv('RAG_UMBRAL', '0.70'))
MAX_CHUNK = int(os.getenv('RAG_MAX_CHUNK', '120'))


def descargar_documentos():
    conn_str = os.getenv('AZURE_STORAGE_CONNECTION')
    container = os.getenv('AZURE_STORAGE_CONTAINER', 'documentos-rag')
    svc = BlobServiceClient.from_connection_string(conn_str)
    container_client = svc.get_container_client(container)
    texto_total = ''
    for blob in container_client.list_blobs():
        texto = svc.get_blob_client(
            container=container, blob=blob.name
        ).download_blob().readall().decode('utf-8')
        texto_total += f'\n\n{texto}'
        print(f'Descargado: {blob.name}')
    return texto_total


def dividir_en_chunks(texto):
    parrafos = [p.strip() for p in texto.split('\n\n') if p.strip()]
    chunks = []
    for p in parrafos:
        palabras = p.split()
        if len(palabras) <= MAX_CHUNK:
            chunks.append(p)
    else:
        inicio = 0
        while inicio < len(palabras):
            chunks.append(' '.join(palabras[inicio:inicio + MAX_CHUNK]))
            inicio += MAX_CHUNK
    return chunks


def crear_embedding(texto):
    resp = client_embedding.embeddings.create(
        model=EMBEDDING_MODEL, input=texto)
    return np.array(resp.data[0].embedding, dtype='float32')


def indexar():
    texto = descargar_documentos()
    chunks = dividir_en_chunks(texto)
    print(f'{len(chunks)} chunks — creando embeddings...')
    vectores = [crear_embedding(c) for c in chunks]
    indice = faiss.IndexFlatIP(len(vectores[0]))
    matriz = np.array(vectores)
    faiss.normalize_L2(matriz)
    indice.add(matriz)
    print(f'Indice FAISS listo: {indice.ntotal} vectores')
    return indice, chunks


def buscar(pregunta, indice, chunks, top_k=3):
    vec = crear_embedding(pregunta).reshape(1, -1)
    faiss.normalize_L2(vec)
    sims, idxs = indice.search(vec, top_k)
    return [{'chunk': chunks[i], 'sim': float(sims[0][j])}
            for j, i in enumerate(idxs[0])]


def responder(pregunta, indice, chunks, verbose=False):
    relevantes = buscar(pregunta, indice, chunks)
    sim_maxima = relevantes[0]['sim']
    if verbose:
        print(f' Similitud maxima: {sim_maxima:.3f} (umbral: {UMBRAL})')
    if sim_maxima < UMBRAL:
        return (f'No encuentro esa informacion en los documentos. '
                f'(sim_max={sim_maxima:.3f} < umbral={UMBRAL})')
    if verbose:
        for i, r in enumerate(relevantes):
            print(f' [{i+1}] sim={r["sim"]:.3f} {r["chunk"][:90]}...')
    contexto = '\n---\n'.join(
        f'[Fragmento {i+1}]\n{r["chunk"]}' for i, r in enumerate(relevantes)
    )
    resp = client_chat.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {'role': 'system', 'content': (
                'Responde EXCLUSIVAMENTE con los fragmentos del contexto. '
                'Si la respuesta no esta en el contexto di exactamente: '
                '"No encuentro esa informacion en los documentos." '
                'Cita siempre el numero de fragmento.'
            )},
            {'role': 'user',
             'content': f'CONTEXTO:\n{contexto}\n\nPREGUNTA: {pregunta}'}
        ],
        temperature=0, max_tokens=400
    )
    return resp.choices[0].message.content


def guardar_indice(indice, chunks, prefijo='mi_indice'):
    faiss.write_index(indice, f'{prefijo}.faiss')
    with open(f'{prefijo}.pkl', 'wb') as f:
        pickle.dump(chunks, f)


def cargar_indice(prefijo='mi_indice'):
    indice = faiss.read_index(f'{prefijo}.faiss')
    with open(f'{prefijo}.pkl', 'rb') as f:
        chunks = pickle.load(f)
    return indice, chunks


# Primera ejecucion: descarga e indexa
indice, chunks = indexar()
guardar_indice(indice, chunks)
# Ejecuciones siguientes (sin coste de embeddings):
# indice, chunks = cargar_indice()
verbose = False
print('RAG listo · Comandos: /verbose /salir')
while True:
    preg = input('Pregunta: ').strip()
    if not preg:
        continue
    if preg == '/salir':
        break
    if preg == '/verbose':
        verbose = not verbose
        print(f'Verbose: {verbose}')
        continue
    print(responder(preg, indice, chunks, verbose))
    print('-' * 50)
    # Ejecutar: python rag.py
