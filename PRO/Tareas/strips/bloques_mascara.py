
import numpy as np

max_operaciones = 14  # número de operaciones distintas

mascara_inicial =int('000100000000', 2)  # PC =Está(B1,3)

# Lista de propiedades PC  para poder realizar la acción
PC = np.zeros(max_operaciones, dtype=int)
# Lista de propiedades a Eliminar de cada acción
E = np.zeros(max_operaciones, dtype=int)
# Lista de propiedades a Añadir de cada acción
A = np.zeros(max_operaciones, dtype=int)


# Definición de operaciones
# Ir(B1,3,4) op=0
PC[0] =int('000100000000', 2)  # PC =Está(B1,3)
E[0] = int('111011000000', 2)  # E = Está(B1,3)
A[0] = int('000010000000', 2)  # A = Está(B1,4)

# Ir(B1,3,5) op=1
PC[1] =int('000100000000', 2)  # PC =Está(B1,3)
E[1] = int('111011000000', 2)  # E = Está(B1,3)
A[1] = int('000001000000', 2)  # A = Está(B1,5)

# Ir(B1,3,1) op=2
PC[2] =int('000110000000', 2)  # PC =Está(B1,3) Está(B2,4) 
E[2] = int('111011000000', 2)  # E = Está(B1,3)
A[2] = int('000001000000', 2)  # A = Está(B1,5)
