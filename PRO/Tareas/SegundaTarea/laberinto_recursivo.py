import numpy as np
import matplotlib.pyplot as plt
import random

# Metodo que retorna un laberinto de un tamaño especificado usando el algoritmo de backtracking generado por chatGPT
def crear_laberinto_backtracking(size):
    # Asegurar tamaño impar
    if size % 2 == 0:
        size += 1

    maze = -1 * np.ones((size, size))  # Laberinto lleno de muros
    stack = [(1, 1)]  # Pila para el backtracking
    maze[1, 1] = 0  # Punto de inicio

    while stack:
        y, x = stack[-1]
        # Vecinos a dos pasos no visitados
        vecinos = [(y+dy, x+dx) for dy, dx in [(-2, 0), (2, 0), (0, -2), (0, 2)]
                   if 1 <= y+dy < size-1 and 1 <= x+dx < size-1 and maze[y+dy, x+dx] == -1]
        if vecinos:
            ny, nx = random.choice(vecinos)
            maze[(y+ny)//2, (x+nx)//2] = 0  # Romper muro
            maze[ny, nx] = 0
            stack.append((ny, nx))
        else:
            stack.pop()

    # Establecer inicio y fin
    maze[1, 1] = 2
    maze[size-2, size-2] = 3

    return maze


# Matriz de movimiento (fila, columna)
move = [
    (0, -1),  # Arriba
    (1, 0),   # Derecha
    (0, 1),   # Abajo
    (-1, 0)   # Izquierda
]


def laberinto_recursivo(maze, y=1, x=1, visitados=None):
    if visitados is None:
        visitados = set()

    visitados.add((y, x))

    # Si es la salida
    if maze[y, x] == 3:
        print("✅ ¡Salida encontrada!")
        return True

    # Marcar el camino
    if maze[y, x] != 3:
        maze[y, x] = 4

    # Intentar todos los movimientos posibles
    for movimiento_y, movimiento_x in move:
        nueva_y, nueva_x = y + movimiento_y, x + movimiento_x
        # Si no ha sido visitado y es camino
        if (nueva_y, nueva_x) not in visitados and maze[nueva_y, nueva_x] in [0, 3]:
            # Llamamos de nuevo al metodo con la nueva posicion y los nodos visitado
            if laberinto_recursivo(maze, nueva_y, nueva_x, visitados):
                return True  # Si encontramos la salida, terminamos

    # Si no se pudo mover a ninguna celda, retroceder
    return False


# Metodo que permite visualizar el laberinto


def visualize_example(x):
    plt.figure()
    plt.imshow(x)
    plt.colorbar()
    plt.grid(False)
    plt.show()


size = 11  # Tamaño del laberinto

laber = crear_laberinto_backtracking(size)
laberinto_recursivo(laber)
visualize_example(laber)
