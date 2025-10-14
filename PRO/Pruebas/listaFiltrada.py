esPar = lambda valor: valor % 2 == 0

lista = [1, 2, 3, 4]

print(list(filter(esPar, lista)))