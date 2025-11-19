from collections import deque
import copy

# -----------------------
# Estado inicial y final
# -----------------------
estado_inicial = [
    [1, 2 ,3 ,4],  # Columna 1
    [],
    []
]

estado_final = [
    [],
    [],
    [4,3,2,1]
]

# -----------------------
# Función para serializar un estado (para comprobar ciclos)
# -----------------------
def serializar(estado):
    return tuple(tuple(pila) for pila in estado)

# -----------------------
# Generar movimientos válidos desde un estado
# -----------------------
def generar_acciones(estado):
    acciones = []
    for i, pila in enumerate(estado):
        if not pila:
            continue
        bloque = pila[-1]  # Solo bloque superior se puede mover
        for j, destino in enumerate(estado):
            if i == j:
                continue
            acciones.append((i, j, bloque))
    return acciones

# -----------------------
# Aplicar acción
# -----------------------
def aplicar_accion(estado, accion):
    i, j, bloque = accion
    nuevo_estado = copy.deepcopy(estado)
    nuevo_estado[i].pop()
    nuevo_estado[j].append(bloque)
    return nuevo_estado

# -----------------------
# BFS para encontrar solución
# -----------------------
cola = deque()
cola.append((estado_inicial, []))  # (estado, secuencia de acciones)
visitados = set()
visitados.add(serializar(estado_inicial))

solucion = None

while cola:
    estado_actual, acciones_realizadas = cola.popleft()

    if estado_actual == estado_final:
        solucion = acciones_realizadas
        break

    for accion in generar_acciones(estado_actual):
        nuevo_estado = aplicar_accion(estado_actual, accion)
        s = serializar(nuevo_estado)
        if s not in visitados:
            visitados.add(s)
            cola.append((nuevo_estado, acciones_realizadas + [accion]))

# -----------------------
# Función para mostrar el estado gráficamente
# -----------------------
def mostrar_estado(estado):
    max_altura = max(len(col) for col in estado)
    columnas = len(estado)
    print("\nEstado actual:")
    for nivel in reversed(range(max_altura)):
        fila = ""
        for col in range(columnas):
            if nivel < len(estado[col]):
                fila += f" {estado[col][nivel]} "
            else:
                fila += " . "
        print(fila)
    print("---" * columnas)

# -----------------------
# Mostrar solución y estado final
# -----------------------
if solucion:
    print("SOLUCIÓN ENCONTRADA:")
    estado_temp = copy.deepcopy(estado_inicial)
    mostrar_estado(estado_temp)
    for idx, acc in enumerate(solucion):
        i,j,bloque = acc
        print(f"Paso {idx+1}: Mover bloque {bloque} de columna {i+1} a columna {j+1}")
        estado_temp = aplicar_accion(estado_temp, acc)
        mostrar_estado(estado_temp)
else:
    print("No se encontró solución")
