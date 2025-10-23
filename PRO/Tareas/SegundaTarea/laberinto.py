import numpy as np
import matplotlib.pyplot as plt
import random

# Metodo que retorna un laberinto de un tamaño especificado con una densidad de muros especificada


def crear_laberinto(size, walls):
    # Laberinto lleno de ceros
    maze = np.zeros((size, size))
    # Establecemos las paredes del laberinto
    maze[0, :] = -1
    maze[:, 0] = -1
    maze[-1, :] = -1
    maze[:, -1] = -1
    # Llenar el laberinto con muros aleatorios
    for y in range(1, size - 1):
        for x in range(1, size - 1):
            if (y, x) not in [(1, 1), (size - 2, size - 2)]:
                if random.random() < walls:
                    maze[y, x] = -1
    # Establecemos el punto de inicio y fin
    maze[1, 1] = 2                  # Inicio
    maze[size - 2, size - 2] = 3    # Fin
    return maze


# Matriz de movimiento (fila, columna)
move = [
    (0, -1),  # Arriba
    (1, 0),   # Derecha
    (0, 1),   # Abajo
    (-1, 0)   # Izquierda
]


def laberinto(maze):
    inicio = (1, 1)
    pila = [inicio]
    visitados = set([inicio])

    while pila:
        y, x = pila[-1]  # Último punto (tope de la pila)

        # Buscar movimiento válido
        moved = False # Marcador de movimiento
        for movimiento_y, movimiento_x in move: # Para cada posible movimiento
            nueva_y, nueva_x = y + movimiento_y, x + movimiento_x # Nueva posición
            # Si no ha sido visitado y es camino
            if (nueva_y, nueva_x) not in visitados and maze[nueva_y, nueva_x] in [0, 3]: #Si no ha sido visitado y es camino
                visitados.add((nueva_y, nueva_x))   # Agregamos a visitados
                if maze[nueva_y, nueva_x] != 3:  # Si no es el final
                    maze[nueva_y, nueva_x] = 4  # Marcamos el camino
                    pila.append((nueva_y, nueva_x))  # Agregamos a la pila
                else: # Si es el final
                    print("✅ ¡Salida encontrada!")
                    return True
                moved = True    # Marcamos que se pudo mover
                break

        # Si no se pudo mover, retroceder
        if not moved:
            pila.pop()  # Sacamos el tope de la pila

    print("❌ No hay salida.")
    return False

# Metodo que permite visualizar el laberinto


def visualize_example(x):
    plt.figure()
    plt.imshow(x)
    plt.colorbar()
    plt.grid(False)
    plt.show()


size = 11  # Tamaño del laberinto
walls = 0.25  # Densidad de los muros

laber = crear_laberinto(size, walls)
laberinto(laber)
visualize_example(laber)
