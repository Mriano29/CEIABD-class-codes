# llamada_simple.py
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
load_dotenv()
client = AzureOpenAI(
    azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
    api_key=os.getenv('AZURE_OPENAI_KEY'),
    api_version=os.getenv('AZURE_OPENAI_API_VERSION')
)
response = client.chat.completions.create(
    model=os.getenv('AZURE_OPENAI_DEPLOYMENT'),
    messages=[
        # system: define el comportamiento base — siempre el primero
        {'role': 'system', 'content': 'Eres un experto en Python.'},
        # user y assistant se alternan para simular la conversación
        {'role': 'user', 'content': '¿Cual es la manera correcta de estructurar fichero?'},
    ]
)
print(response.choices[0].message.content)
# Ejecutar: python llamada_simple.py
