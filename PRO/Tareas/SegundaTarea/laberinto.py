import numpy as np
import matplotlib.pyplot as plt

# Tamaño del laberinto
n = 101

# Crear el MAZE vacío
MAZE = np.zeros((n, n), dtype=int)

# Bordes a 1 (muros)
MAZE[0, :] = 1
MAZE[-1, :] = 1
MAZE[:, 0] = 1
MAZE[:, -1] = 1

# Generar muros internos aleatorios
probabilidad_muro = 0.3
MAZE[1:-1, 1:-1] = (np.random.rand(n-2, n-2) < probabilidad_muro).astype(int)

# Asegurar inicio y fin libres
MAZE[1, 1] = 2     # inicio
MAZE[n-2, n-2] = 3 # fin

# Copia del laberinto para marcar visitas
MARK = MAZE.copy()

# Movimientos: arriba, derecha, abajo, izquierda
MOVE = np.array([
    [-1, 0],
    [0, 1],
    [1, 0],
    [0, -1]
])

# --- DFS recursivo ---
def dfs(x, y):
    # Si llegamos al final
    if MAZE[x, y] == 3:
        print(f"✅ Fin encontrado en ({x}, {y})")
        return True

    # Marcar la celda como visitada
    MARK[x, y] = 4  # 4 = visitado

    # Intentar moverse en las 4 direcciones
    for d in range(4):
        nx = x + MOVE[d, 0]
        ny = y + MOVE[d, 1]

        # Si está dentro de los límites
        if 0 <= nx < n and 0 <= ny < n:
            # Si es un camino libre o el fin
            if MARK[nx, ny] in [0, 3]:
                if dfs(nx, ny):  # llamada recursiva
                    # Marcar el camino correcto (solo si forma parte de la solución)
                    MARK[nx, ny] = 5
                    return True

    return False  # no se encontró camino desde esta rama

# --- Ejecutar búsqueda ---
inicio = (1, 1)
print("🔍 Iniciando búsqueda en profundidad...")
encontrado = dfs(inicio[0], inicio[1])

if encontrado:
    print("🎉 Camino encontrado hasta el objetivo.")
else:
    print("❌ No se encontró camino (el laberinto puede estar bloqueado).")

# --- Visualización ---
def visualize_example(x):
    plt.figure(figsize=(6, 6))
    plt.imshow(x, cmap="tab20c", origin="upper")
    plt.axis('off')
    plt.show()

visualize_example(MARK)
