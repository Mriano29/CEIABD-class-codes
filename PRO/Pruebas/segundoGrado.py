import math

# Pedimos los coeficientes
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

# Comprobamos que a no sea 0 (porque no sería cuadrática)
if a == 0:
    print("Esto no es una ecuación de segundo grado (a no puede ser 0).")
else:
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"Las soluciones reales son: x1 = {x1}, x2 = {x2}")
    elif discriminante == 0:
        x = -b / (2*a)
        print(f"La ecuación tiene una única solución real: x = {x}")
    else:
        real = -b / (2*a)
        imaginaria = math.sqrt(-discriminante) / (2*a)
        print(f"Las soluciones son complejas:")
        print(f"x1 = {real} + {imaginaria}i")
        print(f"x2 = {real} - {imaginaria}i")
