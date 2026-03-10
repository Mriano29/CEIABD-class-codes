# chatbot.py
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
load_dotenv()
client = AzureOpenAI(
    azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT'),
    api_key = os.getenv('AZURE_OPENAI_KEY'),
    api_version = os.getenv('AZURE_OPENAI_API_VERSION')
)
# ✏ CAMBIA ESTE SYSTEM PROMPT — ver y sección 4.1
system_prompt = (
    # 1. Rol específico con credibilidad
    'Eres un experto en Mecanica naval con 30 años de experiencia. '
    # 2. Idioma y tono
    'Respondes SIEMPRE en castellano con tono formal. '
    # 3. Formato de salida
    'Tus respuestas incluyen: (1) explicación concisa, (2) ejemplo práctico. '
    # 4. Restricción negativa — qué NO debe hacer
    'Si la pregunta no es sobre mecanica naval, responde: "Solo puedo ayudarte con temas de embarcaciones."'
)
historial = [
    {'role': 'system', 'content': system_prompt}
]
print('Chatbot Azure OpenAI — escribe "salir" para terminar')
print('-' * 50)
while True:
    pregunta = input('Tu: ').strip()
    if not pregunta: continue
    if pregunta.lower() == 'salir': break
    historial.append({'role': 'user', 'content': pregunta})
    respuesta = client.chat.completions.create(
        model = os.getenv('AZURE_OPENAI_DEPLOYMENT'),
        messages = historial
    )
    mensaje = respuesta.choices[0].message.content
    historial.append({'role': 'assistant', 'content': mensaje})
    print(f'Asistente: {mensaje}')
    print('-' * 50)
# Ejecutar: python chatbot.py