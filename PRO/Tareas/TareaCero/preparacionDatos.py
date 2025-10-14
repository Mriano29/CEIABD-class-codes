import re
import numpy as np
import pandas as pd


def quitarTildes(texto):
    texto = texto.lower()
    replacements = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"))
    for a, b in replacements:
        texto = texto.replace(a, b)
    return texto


def escribirFichero(numero_lineas, ocurrencias_el, textoSinTildes):
    with open('PRO/Tareas/TareaCero/resultado.txt', 'w') as f:
        f.write(f"El texto tiene {numero_lineas} líneas.\n")
        f.write(f"El artículo 'el' aparece {ocurrencias_el} veces.\n")
        f.write(textoSinTildes)


def leerFichero():
    with open('PRO\Tareas\TareaCero\FicheroALeer.txt', 'r') as f:
        # Leer todo el contenido del archivo como un string
        texto = f.read()
        # Numero de lineas
        numero_lineas = len(texto.splitlines())
        # Texto sin tildes
        textoSinTildes = quitarTildes(texto)
        # Buscar todas las apariciones de 'el' como palabra completa, sin distinguir mayúsculas/minúsculas
        ocurrencias_el = len(re.findall(r'\bel\b', textoSinTildes, re.IGNORECASE))
        # Resultados
        print("Texto contenido en el archivo:", end="\n")
        print(texto)
        print("\n\n")
        print(f"El texto tiene {numero_lineas} líneas.")
        print(f"El artículo 'el' aparece {ocurrencias_el} veces.")
        print("\n\n")
        print("Texto en minuscula sin tildes:", end="\n")
        print(textoSinTildes)
        escribirFichero(numero_lineas, ocurrencias_el, textoSinTildes)


def librerias():
    # Csv inicial
    poblacion = pd.read_csv('PRO\Tareas\TareaCero\poblacionMunicipios.csv')

    # Eliminar filas con valores NaN o 0 en la columna 'poblacion'
    poblacion_limpia = poblacion.dropna(subset=['Poblacion'])
    poblacion_limpia = poblacion_limpia[poblacion_limpia['Poblacion'] > 0]

    total_por_municipio = poblacion.groupby(by='Municipio').sum()
    print(total_por_municipio)


    # Resultados
    print(poblacion)
    print(poblacion_limpia)
    print(poblacion['Poblacion'])

librerias()