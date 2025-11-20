# ================================================================
# GENERADOR DE MÁSCARAS BINARIAS EN FORMATO TIPO:
# PC[i]=int('xxxxxxxxxxxxx',2)
# E[i] =int('xxxxxxxxxxxxx',2)
# A[i] =int('xxxxxxxxxxxxx',2)
# ================================================================

# -----------------------------------------------------------
# 1. DEFINICIÓN DEL MAPEADO DE PREDICADOS → POSICIÓN DE BIT
# -----------------------------------------------------------
# (Puedes cambiar aquí los predicados y sus bits)

PREDICADOS = {
    # bit : etiqueta
    12: "On(A,B)",
    11: "On(B,A)",
    10: "OnTable(A,0)",
    9:  "OnTable(A,1)",
    8:  "OnTable(A,2)",
    7:  "OnTable(B,0)",
    6:  "OnTable(B,1)",
    5:  "OnTable(B,2)",
    4:  "Clear(A)",
    3:  "Clear(B)",
    2:  "ClearCol(0)",
    1:  "ClearCol(1)",
    0:  "ClearCol(2)",
}

# predicado ⇒ máscara binaria
BIT = { name: (1 << bit) for bit, name in PREDICADOS.items() }


# -----------------------------------------------------------
# 2. DEFINICIÓN DE PLANTILLAS DE ACCIONES PARAMÉTRICAS
# -----------------------------------------------------------

ACCIONES_PARAMETRICAS = [

    # ------------------------- PickUp -------------------------
    ("PickUp", ["A","B"], [0,1,2],
     lambda x, c: {
         "PC": [f"Clear({x})", f"OnTable({x},{c})", f"ClearCol({c})"],
         "E":  [f"OnTable({x},{c})"],
         "A":  []              # sin bit de Holding
     }),

    # ------------------------- PutDown -------------------------
    ("PutDown", ["A","B"], [0,1,2],
     lambda x, c: {
         "PC": [f"ClearCol({c})"],
         "E":  [],
         "A":  [f"OnTable({x},{c})"]
     }),

    # ------------------------- Stack x sobre y -------------------------
    ("Stack", ["A","B"], ["A","B"], [0,1,2],
     lambda x, y, c: {} if x==y else {
         "PC": [f"Clear({y})", f"ClearCol({c})"],
         "E":  [f"Clear({y})"],
         "A":  [f"On({x},{y})"]
     }),

    # ------------------------- Unstack x de sobre y -------------------------
    ("Unstack", ["A","B"], ["A","B"], [0,1,2],
     lambda x, y, c: {} if x==y else {
         "PC": [f"On({x},{y})", f"Clear({x})"],
         "E":  [f"On({x},{y})"],
         "A":  [f"Clear({y})"]
     }),
]

# -----------------------------------------------------------
# 3. MOTOR GENERADOR
# -----------------------------------------------------------

def lista_a_mascara(lista_predicados):
    m = 0
    for p in lista_predicados:
        if p in BIT:
            m |= BIT[p]
    return m

op = 0
resultados = []

for entry in ACCIONES_PARAMETRICAS:

    # detectamos número de argumentos según longitud de la tupla
    if len(entry) == 4:
        nombre, args1, args2, fn = entry
        for x in args1:
            for c in args2:
                dic = fn(x,c)
                if not dic: continue
                PC = lista_a_mascara(dic["PC"])
                E  = lista_a_mascara(dic["E"])
                A  = lista_a_mascara(dic["A"])
                resultados.append( (op, nombre, (x,c), PC, E, A) )
                op += 1

    elif len(entry) == 5:
        nombre, args1, args2, args3, fn = entry
        for x in args1:
            for y in args2:
                for c in args3:
                    dic = fn(x,y,c)
                    if not dic: continue
                    PC = lista_a_mascara(dic["PC"])
                    E  = lista_a_mascara(dic["E"])
                    A  = lista_a_mascara(dic["A"])
                    resultados.append( (op, nombre, (x,y,c), PC, E, A) )
                    op += 1


# -----------------------------------------------------------
# 4. IMPRIMIR RESULTADO EN FORMATO EXACTO DE TU EJEMPLO
# -----------------------------------------------------------

for op_id, nom, params, PC, E, A in resultados:
    print("#----------------------------------------------------")
    print(f"# {nom}{params} op={op_id}")
    print(f"PC[{op_id}] = int('{PC:013b}', 2)")
    print(f"E[{op_id}]  = int('{E:013b}', 2)")
    print(f"A[{op_id}]  = int('{A:013b}', 2)")
