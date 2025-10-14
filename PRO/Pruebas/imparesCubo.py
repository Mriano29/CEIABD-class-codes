numbers = []

for i in range(1,11):
    numbers.append(i)

impares = lambda valor: valor % 2 != 0
cubo = lambda valor: valor**3

print(list(map(cubo, list(filter(impares, numbers)))))