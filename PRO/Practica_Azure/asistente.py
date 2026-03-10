# asistente.py — Parte 1: setup y configuración
import os
import tiktoken
from dotenv import load_dotenv
from openai import AzureOpenAI
load_dotenv()
client = AzureOpenAI(
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    api_key=os.getenv('AZURE_OPENAI_KEY'),
    api_version=os.getenv('AZURE_OPENAI_API_VERSION')
)
deployment = os.getenv('AZURE_OPENAI_DEPLOYMENT')
enc = tiktoken.encoding_for_model('gpt-4o')
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ✏ MODIFICA este bloque para personalizar el asistente
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
CONFIG = {
    'system_prompt': (
        # Cambia esto por tu system prompt profesional (4 componentes)
        'Eres un asistente técnico experto en Python con 10 años de experiencia. '
        'Respondes SIEMPRE en castellano con un tono claro y profesional. '
        'Tus respuestas incluyen: (1) explicación concisa, (2) ejemplo de código práctico, (3) recomendaciones o buenas prácticas. '
        'Si la pregunta no es sobre Python, responde: "Solo puedo ayudarte con Python."'
    ),
    'temperature': 0.2,  # tecnico preciso
    'max_tokens': 500,  # max respuesta corta
    'top_p': 0.5, # tecnico preciso
    'frequency_penalty': 0.0,
    'presence_penalty': 0.0,
    'max_historial': 2,  # prueba con 2 para ver que 'olvida'
}


def contar_tokens(messages):
    return sum(len(enc.encode(m['content'])) for m in messages)


def chat(historial, pregunta):
    historial.append({'role': 'user', 'content': pregunta})
    system = [{'role': 'system', 'content': CONFIG['system_prompt']}]
    reciente = historial[-(CONFIG['max_historial'] * 2):]
    response = client.chat.completions.create(
        model=deployment,
        messages=system + reciente,
        temperature=CONFIG['temperature'],
        max_tokens=CONFIG['max_tokens'],
        top_p=CONFIG['top_p'],
        frequency_penalty=CONFIG['frequency_penalty'],
        presence_penalty=CONFIG['presence_penalty'],
    )
    respuesta = response.choices[0].message.content
    historial.append({'role': 'assistant', 'content': respuesta})
    return respuesta, response.usage.prompt_tokens, response.usage.completion_tokens


historial = []
print('Asistente · Comandos: /config /reset /tokens salir')
print('=' * 55)
while True:
    entrada = input('Tu: ').strip()
    if not entrada: continue
    if entrada == 'salir': break
    if entrada == '/config':
        [print(f' {k}: {v}') for k, v in CONFIG.items() if k != 'system_prompt']
        continue
    if entrada == '/reset':
        historial = []; print('[Historial borrado]'); continue
    if entrada == '/tokens':
        msgs = [{'role':'system','content':CONFIG['system_prompt']}] + historial
        print(f'[Tokens en contexto: {contar_tokens(msgs)}]'); continue
    resp, p_tok, c_tok = chat(historial, entrada)
    print(f'Asistente: {resp}')
    print(f'[entrada={p_tok} | respuesta={c_tok} tokens]')
    print('-' * 55)
# Ejecutar: python asistente.py
