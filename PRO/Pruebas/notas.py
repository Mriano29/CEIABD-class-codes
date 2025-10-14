listaNotas = [-1,0,1,2,3,4,5,6,7,8,9,10,11,'abc']

def calcularNota(nota):
    #nota = float(input("Introduce la nota del alumno: "))
    if(type(nota) != int):
        print("Formato erróneo")
    else:    
        if(nota > 10 or nota < 0):
            print("Nota incorrecta")
        else:
            if(nota > 5):
                if(nota > 7):
                    print("Nota sobresaliente")
                else:
                    print("Nota aprobatoria")
            else:
                if(nota == 5):
                    print("Nota aprobatoria")
                else:
                    print("Suspenso")



for i in range(len(listaNotas)):
    calcularNota(listaNotas[i])