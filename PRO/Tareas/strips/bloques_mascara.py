
import numpy as np

max_profundidad = 5  # Inteligencia del mono
max_operaciones = 36  # número de operaciones distintas
estado = np.zeros(max_profundidad, dtype=int)  # Pila de estados
operaciones = np.zeros(max_profundidad, dtype=int)  # Pila de operaciones

# Lista de propiedades PC  para poder realizar la acción
PC = np.zeros(max_operaciones, dtype=int)
# Lista de propiedades a Eliminar de cada acción
E = np.zeros(max_operaciones, dtype=int)
# Lista de propiedades a Añadir de cada acción
A = np.zeros(max_operaciones, dtype=int)

texto = [
    "Ir(B1,3,4)",  # 0
    "Ir(B1,3,5)",  # 1
    "Ir(B1,3,1)",  # 2
    "Ir(B1,3,2)",  # 3
    "Ir(B1,4,3)",  # 4
    "Ir(B1,4,5)",  # 5
    "Ir(B1,4,0)",  # 6
    "Ir(B1,4,2)",  # 7
    "Ir(B1,5,3)",  # 8
    "Ir(B1,5,4)",  # 9
    "Ir(B1,5,0)",  # 10
    "Ir(B1,5,1)",  # 11
    "Ir(B1,0,4)",  # 12
    "Ir(B1,0,5)",  # 13
    "Ir(B1,2,4)",  # 14
    "Ir(B1,2,3)",  # 15
    "Ir(B1,1,3)",  # 16
    "Ir(B1,1,5)",  # 17
    "Ir(B2,3,4)",  # 18
    "Ir(B2,3,5)",  # 19
    "Ir(B2,3,1)",  # 20
    "Ir(B2,3,2)",  # 21
    "Ir(B2,4,3)",  # 22
    "Ir(B2,4,5)",  # 23
    "Ir(B2,4,0)",  # 24
    "Ir(B2,4,2)",  # 25
    "Ir(B2,5,3)",  # 26
    "Ir(B2,5,4)",  # 27
    "Ir(B2,5,0)",  # 28
    "Ir(B2,5,1)",  # 29
    "Ir(B2,0,4)",  # 30
    "Ir(B2,0,5)",  # 31
    "Ir(B2,2,4)",  # 32
    "Ir(B2,2,3)",  # 33
    "Ir(B2,1,3)",  # 34
    "Ir(B2,1,5)"   # 35
]


# Definición de operaciones
# Ir(B1,3,4)
PC[0] = int('000100000001', 2)  # PC =Está(B1,3) Está(B2,5)
E[0] = int('111011000000', 2)  # E = Está(B1,3)
A[0] = int('000010000001', 2)  # A = Está(B1,4)

# Ir(B1,3,5)
PC[1] = int('000100000010', 2)  # PC =Está(B1,3) Está(B2,4)
E[1] = int('111011000000', 2)  # E = Está(B1,3)
A[1] = int('000001000010', 2)  # A = Está(B1,5)

# Ir(B1,3,1)
PC[2] = int('000100000010', 2)  # PC =Está(B1,3) Está(B2,4)
E[2] = int('111011000000', 2)  # E = Está(B1,3)
A[2] = int('010000000010', 2)  # A = Está(B1,1)

# Ir(B1,3,2)
PC[3] = int('000100000001', 2)  # PC =Está(B1,3) Está(B2,5)
E[3] = int('111011000000', 2)  # E = Está(B1,3)
A[3] = int('001000000001', 2)  # A = Está(B1,1)

# -----------------------------------------------------------

# Ir(B1,4,3)
PC[4] = int('000010000001', 2)  # PC =Está(B1,4) Está(B2,5)
E[4] = int('111101000000', 2)  # E = Está(B1,4)
A[4] = int('000100000001', 2)  # A = Está(B1,3)

# Ir(B1,4,5)
PC[5] = int('000010000100', 2)  # PC =Está(B1,4) Está(B2,3)
E[5] = int('111101000000', 2)  # E = Está(B1,4)
A[5] = int('000001000100', 2)  # A = Está(B1,5)

# Ir(B1,4,0)
PC[6] = int('000010000100', 2)  # PC =Está(B1,4) Está(B2,3)
E[6] = int('111101000000', 2)  # E = Está(B1,4)
A[6] = int('100000000100', 2)  # A = Está(B1,0)

# Ir(B1,4,2)
PC[7] = int('000010000001', 2)  # PC =Está(B1,4) Está(B2,5)
E[7] = int('111101000000', 2)  # E = Está(B1,4)
A[7] = int('001000000001', 2)  # A = Está(B1,2)

# -----------------------------------------------------------

# Ir(B1,5,3)
PC[8] = int('000001000010', 2)  # PC =Está(B1,5) Está(B2,4)
E[8] = int('111110000000', 2)  # E = Está(B1,5)
A[8] = int('000100000010', 2)  # A = Está(B1,3)

# Ir(B1,5,4)
PC[9] = int('000001000100', 2)  # PC =Está(B1,5) Está(B2,3)
E[9] = int('111110000000', 2)  # E = Está(B1,5)
A[9] = int('000010000100', 2)  # A = Está(B1,4)

# Ir(B1,5,0)
PC[10] = int('000001000100', 2)  # PC =Está(B1,5) Está(B2,3)
E[10] = int('111110000000', 2)  # E = Está(B1,5)
A[10] = int('100000000100', 2)  # A = Está(B1,0)

# Ir(B1,5,1)
PC[11] = int('000001000010', 2)  # PC =Está(B1,5) Está(B2,4)
E[11] = int('111110000000', 2)  # E = Está(B1,5)
A[11] = int('010000000010', 2)  # A = Está(B1,1)

# -----------------------------------------------------------

# Ir(B1,0,4)
PC[12] = int('100000000100', 2)  # PC =Está(B1,0) Está(B2,3)
E[12] = int('011111000000', 2)  # E = Está(B1,0)
A[12] = int('000010000100', 2)  # A = Está(B1,4)

# Ir(B1,0,5)
PC[13] = int('100000000100', 2)  # PC =Está(B1,0) Está(B2,3)
E[13] = int('011111000000', 2)  # E = Está(B1,0)
A[13] = int('000001000100', 2)  # A = Está(B1,5)

# -----------------------------------------------------------

# Ir(B1,2,4)
PC[14] = int('001000000001', 2)  # PC =Está(B1,2) Está(B2,5)
E[14] = int('110111000000', 2)  # E = Está(B1,2)
A[14] = int('000010000001', 2)  # A = Está(B1,4)

# Ir(B1,2,3)
PC[15] = int('001000000001', 2)  # PC =Está(B1,0) Está(B2,5)
E[15] = int('110111000000', 2)  # E = Está(B1,0)
A[15] = int('000001000001', 2)  # A = Está(B1,5)

# -----------------------------------------------------------

# Ir(B1,1,3)
PC[16] = int('010000000010', 2)  # PC =Está(B1,1) Está(B2,4)
E[16] = int('101111000000', 2)  # E = Está(B1,1)
A[16] = int('000001000010', 2)  # A = Está(B1,5)

# Ir(B1,1,5)
PC[17] = int('010000000010', 2)  # PC =Está(B1,0) Está(B2,3)
E[17] = int('101111000000', 2)  # E = Está(B1,0)
A[17] = int('000001000010', 2)  # A = Está(B1,5)

# -----------------------------------------------------------

# Ir(B2,3,4)
PC[18] = int('000001000100', 2)
E[18] = int('000000111011', 2)
A[18] = int('000000100010', 2)

# Ir(B2,3,5)
PC[19] = int('000010000100', 2)
E[19] = int('000000111011', 2)
A[19] = int('000001000001', 2)

# Ir(B2,3,1)
PC[20] = int('000010000100', 2)
E[20] = int('000000111011', 2)
A[20] = int('000010010000', 2)

# Ir(B2,3,2)
PC[21] = int('000001000100', 2)
E[21] = int('000000111011', 2)
A[21] = int('000001001000', 2)

# -----------------------------------------------------------

# Ir(B2,4,3)
PC[22] = int('000001000010', 2)
E[22] = int('000000111101', 2)
A[22] = int('000001000100', 2)

# Ir(B2,4,5)
PC[23] = int('000100000010', 2)
E[23] = int('000000111101', 2)
A[23] = int('000100000001', 2)

# Ir(B2,4,0)
PC[24] = int('000100000010', 2)
E[24] = int('000000111101', 2)
A[24] = int('000100100000', 2)

# Ir(B2,4,2)
PC[25] = int('000001000010', 2)
E[25] = int('000000111101', 2)
A[25] = int('000001001000', 2)

# -----------------------------------------------------------

# Ir(B2,5,3)
PC[26] = int('000010000001', 2)
E[26] = int('000000111110', 2)
A[26] = int('000010000100', 2)

# Ir(B2,5,4)
PC[27] = int('000100000001', 2)
E[27] = int('000000111110', 2)
A[27] = int('000100000010', 2)

# Ir(B2,5,0)
PC[28] = int('000100000001', 2)
E[28] = int('000000111110', 2)
A[28] = int('000100100000', 2)

# Ir(B2,5,1)
PC[29] = int('000010000001', 2)
E[29] = int('000000111110', 2)
A[29] = int('000010010000', 2)

# -----------------------------------------------------------

# Ir(B2,0,4)
PC[30] = int('000100100000', 2)
E[30] = int('000000011111', 2)
A[30] = int('000100000010', 2)

# Ir(B2,0,5)
PC[31] = int('000100100000', 2)
E[31] = int('000000011111', 2)
A[31] = int('000100000001', 2)

# -----------------------------------------------------------

# Ir(B2,2,4)
PC[32] = int('000001001000', 2)
E[32] = int('000000110111', 2)
A[32] = int('000001000010', 2)

# Ir(B2,2,3)
PC[33] = int('000001001000', 2)
E[33] = int('000000110111', 2)
A[33] = int('000001000001', 2)

# -----------------------------------------------------------

# Ir(B2,1,3)
PC[34] = int('000010010000', 2)
E[34] = int('000000101111', 2)
A[34] = int('000010000100', 2)

# Ir(B2,1,5)
PC[35] = int('000010010000', 2)
E[35] = int('000000101111', 2)
A[35] = int('000010000001', 2)


# ----------------------------------------------------------------------------------------------------
vectorInicial = [4, 1]
vectorFinal = [3, 6]


def mascaraInicio():
    mascara = ''
    if (vectorInicial[0] == 1):
        mascara = "100000"  # Está(M,1)
    if (vectorInicial[0] == 2):
        mascara = "010000"  # Está(M,2)
    if (vectorInicial[0] == 3):
        mascara = "001000"  # Está(M,3)
    if (vectorInicial[0] == 4):
        mascara = "000100"  # Está(M,1)
    if (vectorInicial[0] == 5):
        mascara = "000010"  # Está(M,2)
    if (vectorInicial[0] == 6):
        mascara = "000001"  # Está(M,3)
    if (vectorInicial[1] == 1):
        mascara += "100000"  # Está(M,1)
    if (vectorInicial[1] == 2):
        mascara += "010000"  # Está(M,2)
    if (vectorInicial[1] == 3):
        mascara += "001000"  # Está(M,3)
    if (vectorInicial[1] == 4):
        mascara += "000100"  # Está(M,1)
    if (vectorInicial[1] == 5):
        mascara += "000010"  # Está(M,2)
    if (vectorInicial[1] == 6):
        mascara += "000001"  # Está(M,3)
    return mascara


def mascaraFin():
    mascara = ''
    if (vectorFinal[0] == 1):
        mascara = "100000"  # Está(M,1)
    if (vectorFinal[0] == 2):
        mascara = "010000"  # Está(M,2)
    if (vectorFinal[0] == 3):
        mascara = "001000"  # Está(M,3)
    if (vectorFinal[0] == 4):
        mascara = "000100"  # Está(M,1)
    if (vectorFinal[0] == 5):
        mascara = "000010"  # Está(M,2)
    if (vectorFinal[0] == 6):
        mascara = "000001"  # Está(M,3)
    if (vectorFinal[1] == 1):
        mascara += "100000"  # Está(M,1)
    if (vectorFinal[1] == 2):
        mascara += "010000"  # Está(M,2)
    if (vectorFinal[1] == 3):
        mascara += "001000"  # Está(M,3)
    if (vectorFinal[1] == 4):
        mascara += "000100"  # Está(M,1)
    if (vectorFinal[1] == 5):
        mascara += "000010"  # Está(M,2)
    if (vectorFinal[1] == 6):
        mascara += "000001"  # Está(M,3)
    return mascara


def intentar(nodo, op):
    # Cumple las PC para aplicar la op
    if (int(bin(nodo & PC[op]), 2) == int(bin(PC[op]), 2)):
        # print(bin(estado), "cumple con:",bin(PC[op]), texto[op])
        sigu = int(bin(nodo & E[op]), 2)  # Eliminamos propiedades E
        # print("Eliminamos ",bin(E[op])," y queda:",bin(siguiente))
        sigu = int(bin(sigu | A[op]), 2)  # Añade propiedades A
        # print("Añadimos ",bin(A[op])," y queda:",bin(siguiente))
        # print(texto[op],'->',end=""
    else:
        sigu = -1
    return sigu
# -------------------------------------------------------------------------------------------------------


def encontrado(siguiente):
    # Aquí comprobamos que no hemos pasado por ese estado
    encontrado = False
    t = top
    while (t >= 0):
        if (estado[t] == siguiente):
            encontrado = True
        t -= 1
    return encontrado


# -------------------------------------------------------------------------------------------------------


# Estado inicial con la secuencia binaria de propiedades
inicial = int(mascaraInicio(), 2)
# meta=   int('0000100100101' , 2 ) # Está(C,2)Está(P,2)Sobre(M,C)Tiene(M,P)
meta = int(mascaraFin(), 2)
# Lista para guardar la secuencia de la solución
solucion_acciones = []

top = 0
estado[top] = inicial
operaciones[top] = 0
op = 0
actual = inicial

while top >= 0:
    while (op < max_operaciones) and (top < max_profundidad - 1) and (actual != meta):
        siguiente = intentar(actual, op)
        if siguiente != -1 and not encontrado(siguiente):
            # Guardamos la acción en la secuencia temporal
            solucion_acciones.append((actual, op, siguiente))

            top += 1
            estado[top] = actual
            operaciones[top] = op
            actual = siguiente
            op = -1
        op += 1

    if int(bin(actual & meta), 2) == int(bin(meta), 2):
        # Solo mostramos la tabla de la solución final
        print("Tabla de acciones de la solución:")
        print(
            f"{'Estado':12} | {'Accion':15} | {'PC':12} | {'E':12} | {'Resultado':12}")
        print("-"*70)
        for estado_act, op_index, resultado in solucion_acciones:
            print(
                f"{format(estado_act,'012b')} | {texto[op_index]:15} | {format(PC[op_index],'012b')} | {format(E[op_index],'012b')} | {format(resultado,'012b')}")

        # Mostramos la secuencia de la solución
        print("\nSOLUCIÓN:")
        print(" --> ".join([texto[op_index]
              for _, op_index, _ in solucion_acciones]))
        top = 0

    actual = estado[top]
    op = operaciones[top] + 1
    top -= 1
    # Limpiamos la secuencia temporal si retrocedemos
    if top < len(solucion_acciones) - 1:
        solucion_acciones = solucion_acciones[:top+1]
