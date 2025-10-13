import numpy as np

matriz = np.empty((0, 3), int)  # matriz vacía con 3 columnas
fila = np.array([1, 2, 3])

for i in range(3):  # tres filas
    matriz = np.append(matriz, [fila], axis=0)

print(matriz)