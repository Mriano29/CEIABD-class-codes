
import numpy as np

# número de operaciones distintas (actualizado para cubrir índices 0..35)
max_operaciones = 36

mascara_inicial = int('000100000001', 2)  # PC = Está(B1,3)  Está(B2,5)

# Lista de propiedades PC  para poder realizar la acción
PC = np.zeros(max_operaciones, dtype=int)
# Lista de propiedades a Eliminar de cada acción
E = np.zeros(max_operaciones, dtype=int)
# Lista de propiedades a Añadir de cada acción
A = np.zeros(max_operaciones, dtype=int)


# Definición de operaciones
# Ir(B1,3,4)
PC[0] = int('000100000001', 2)  # PC =Está(B1,3) Está(B2,5)
E[0] = int('111011000000', 2)  # E = Está(B1,3)
A[0] = int('000010000000', 2)  # A = Está(B1,4)

# Ir(B1,3,5)
PC[1] = int('000100000010', 2)  # PC =Está(B1,3) Está(B2,4)
E[1] = int('111011000000', 2)  # E = Está(B1,3)
A[1] = int('000001000000', 2)  # A = Está(B1,5)

# Ir(B1,3,1)
PC[2] = int('000100000010', 2)  # PC =Está(B1,3) Está(B2,4)
E[2] = int('111011000000', 2)  # E = Está(B1,3)
A[2] = int('010000000000', 2)  # A = Está(B1,1)

# Ir(B1,3,2)
PC[3] = int('000100000001', 2)  # PC =Está(B1,3) Está(B2,5)
E[3] = int('111011000000', 2)  # E = Está(B1,3)
A[3] = int('001000000000', 2)  # A = Está(B1,1)

# -----------------------------------------------------------

# Ir(B1,4,3)
PC[4] = int('000010000001', 2)  # PC =Está(B1,4) Está(B2,5)
E[4] = int('111101000000', 2)  # E = Está(B1,4)
A[4] = int('000100000000', 2)  # A = Está(B1,3)

# Ir(B1,4,5)
PC[5] = int('000010000100', 2)  # PC =Está(B1,4) Está(B2,3)
E[5] = int('111101000000', 2)  # E = Está(B1,4)
A[5] = int('000001000000', 2)  # A = Está(B1,5)

# Ir(B1,4,0)
PC[6] = int('000010000100', 2)  # PC =Está(B1,4) Está(B2,3)
E[6] = int('111101000000', 2)  # E = Está(B1,4)
A[6] = int('100000000000', 2)  # A = Está(B1,0)

# Ir(B1,4,2)
PC[7] = int('000010000001', 2)  # PC =Está(B1,4) Está(B2,5)
E[7] = int('111101000000', 2)  # E = Está(B1,4)
A[7] = int('001000000000', 2)  # A = Está(B1,2)

# -----------------------------------------------------------

# Ir(B1,5,3)
PC[8] = int('000001000010', 2)  # PC =Está(B1,5) Está(B2,4)
E[8] = int('111110000000', 2)  # E = Está(B1,5)
A[8] = int('000100000000', 2)  # A = Está(B1,3)

# Ir(B1,5,4)
PC[9] = int('000001000100', 2)  # PC =Está(B1,5) Está(B2,3)
E[9] = int('111110000000', 2)  # E = Está(B1,5)
A[9] = int('000010000000', 2)  # A = Está(B1,4)

# Ir(B1,5,0)
PC[10] = int('000001000100', 2)  # PC =Está(B1,5) Está(B2,3)
E[10] = int('111110000000', 2)  # E = Está(B1,5)
A[10] = int('100000000000', 2)  # A = Está(B1,0)

# Ir(B1,5,1)
PC[11] = int('000001000010', 2)  # PC =Está(B1,5) Está(B2,4)
E[11] = int('111110000000', 2)  # E = Está(B1,5)
A[11] = int('010000000000', 2)  # A = Está(B1,1)

# -----------------------------------------------------------

# Ir(B1,0,4)
PC[12] = int('100000000100', 2)  # PC =Está(B1,0) Está(B2,3)
E[12] = int('011111000000', 2)  # E = Está(B1,0)
A[12] = int('000010000000', 2)  # A = Está(B1,4)

# Ir(B1,0,5)
PC[13] = int('100000000100', 2)  # PC =Está(B1,0) Está(B2,3)
E[13] = int('011111000000', 2)  # E = Está(B1,0)
A[13] = int('000001000000', 2)  # A = Está(B1,5)

# -----------------------------------------------------------

# Ir(B1,2,4)
PC[14] = int('001000000001', 2)  # PC =Está(B1,2) Está(B2,5)
E[14] = int('110111000000', 2)  # E = Está(B1,2)
A[14] = int('000010000000', 2)  # A = Está(B1,4)

# Ir(B1,2,3)
PC[15] = int('001000000001', 2)  # PC =Está(B1,0) Está(B2,5)
E[15] = int('110111000000', 2)  # E = Está(B1,0)
A[15] = int('000001000000', 2)  # A = Está(B1,5)

# -----------------------------------------------------------

# Ir(B1,1,3)
PC[16] = int('010000000010', 2)  # PC =Está(B1,1) Está(B2,4)
E[16] = int('101111000000', 2)  # E = Está(B1,1)
A[16] = int('000001000000', 2)  # A = Está(B1,5)

# Ir(B1,1,5)
PC[17] = int('010000000010', 2)  # PC =Está(B1,0) Está(B2,3)
E[17] = int('101111000000', 2)  # E = Está(B1,0)
A[17] = int('000001000000', 2)  # A = Está(B1,5)

# -----------------------------------------------------------

# Ir(B2,3,4)
PC[18] = int('000001000100', 2)
E[18] = int('000000111011', 2)
A[18] = int('000000000010', 2)

# Ir(B2,3,5)
PC[19] = int('000010000100', 2)
E[19] = int('000000111011', 2)
A[19] = int('000000000001', 2)

# Ir(B2,3,1)
PC[20] = int('000010000100', 2)
E[20] = int('000000111011', 2)
A[20] = int('000000010000', 2)

# Ir(B2,3,2)
PC[21] = int('000001000100', 2)
E[21] = int('000000111011', 2)
A[21] = int('000000001000', 2)

# -----------------------------------------------------------

# Ir(B2,4,3)
PC[22] = int('000001000010', 2)
E[22] = int('000000111101', 2)
A[22] = int('000000000100', 2)

# Ir(B2,4,5)
PC[23] = int('000100000010', 2)
E[23] = int('000000111101', 2)
A[23] = int('000000000001', 2)

# Ir(B2,4,0)
PC[24] = int('000100000010', 2)
E[24] = int('000000111101', 2)
A[24] = int('000000100000', 2)

# Ir(B2,4,2)
PC[25] = int('000001000010', 2)
E[25] = int('000000111101', 2)
A[25] = int('000000001000', 2)

# -----------------------------------------------------------

# Ir(B2,5,3)
PC[26] = int('000010000001', 2)
E[26] = int('000000111110', 2)
A[26] = int('000000000100', 2)

# Ir(B2,5,4)
PC[27] = int('000100000001', 2)
E[27] = int('000000111110', 2)
A[27] = int('000000000010', 2)

# Ir(B2,5,0)
PC[28] = int('000100000001', 2)
E[28] = int('000000111110', 2)
A[28] = int('000000100000', 2)

# Ir(B2,5,1)
PC[29] = int('000010000001', 2)
E[29] = int('000000111110', 2)
A[29] = int('000000010000', 2)

# -----------------------------------------------------------

# Ir(B2,0,4)
PC[30] = int('000100100000', 2)
E[30] = int('000000011111', 2)
A[30] = int('000000000010', 2)

# Ir(B2,0,5)
PC[31] = int('000100100000', 2)
E[31] = int('000000011111', 2)
A[31] = int('000000000001', 2)

# -----------------------------------------------------------

# Ir(B2,2,4)
PC[32] = int('000001001000', 2)
E[32] = int('000000110111', 2)
A[32] = int('000000000010', 2)

# Ir(B2,2,3)
PC[33] = int('000001001000', 2)
E[33] = int('000000110111', 2)
A[33] = int('000000000001', 2)

# -----------------------------------------------------------

# Ir(B2,1,3)
PC[34] = int('000010010000', 2)
E[34] = int('000000101111', 2)
A[34] = int('000000000001', 2)

# Ir(B2,1,5)
PC[35] = int('000010010000', 2)
E[35] = int('000000101111', 2)
A[35] = int('000000000001', 2)


def dfs_planning():
    # Estado inicial (PC válido)
    initial_state = int('000100000001', 2)  # PC[0]: B1=3, B2=5
    
    # Estado objetivo (debe ser un PC válido)
    goal_state = int('000001001000', 2)     # PC[32]: B1=5, B2=2
    
    # Verificar que el objetivo es un PC válido
    is_goal_valid_pc = any(PC[i] == goal_state for i in range(36))
    print(f"¿Estado objetivo es PC válido? {is_goal_valid_pc}")
    
    # Estructuras para DFS
    stack = [(initial_state, [])]
    visited = set([initial_state])
    
    while stack:
        current_state, current_plan = stack.pop()
        
        # Verificar si alcanzamos el objetivo
        if current_state == goal_state:
            return current_plan, current_state
        
        # Probar todas las operaciones
        for i in range(36):
            # Verificar precondiciones
            if (current_state & PC[i]) == PC[i]:
                # Aplicar la operación
                new_state = (current_state & ~E[i]) | A[i]
                
                # Si no hemos visitado este estado y es un PC válido
                if new_state not in visited and any(PC[j] == new_state for j in range(36)):
                    visited.add(new_state)
                    new_plan = current_plan + [f"Op_{i}"]
                    stack.append((new_state, new_plan))
    
    return None, None

# Ejecutar DFS
plan, final_state = dfs_planning()

if plan:
    print("\n¡Plan encontrado!")
    for i, action in enumerate(plan, 1):
        # Mostrar qué operación se ejecutó
        op_num = int(action.split('_')[1])
        print(f"Paso {i}: {action} -> Mueve de {bin(PC[op_num])[2:].zfill(12)} a {bin(A[op_num])[2:].zfill(12)}")
    print(f"Estado final: {bin(final_state)[2:].zfill(12)}")
else:
    print("No se encontró plan")