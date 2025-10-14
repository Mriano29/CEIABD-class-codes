import math

class circunsferencia:
    
    def __init__(self,radio):
        self.radio = radio

    def area(self):
        resultado = math.pi * self.radio**2
        return resultado

    def longitud(self):
        resultado = 2 * math.pi * self.radio
        return resultado

class rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        resultado = self.base * self.altura
        return resultado


class cilindro:    
    def __init__(self, circunsferencia, rectangulo):
        self.circunsferencia = circunsferencia
        self.rectangulo = rectangulo
        
    def area(self):
        areaCircunsferencia = self.circunsferencia.area()
        areaRectangulo = self.rectangulo.area()
        resultado = areaCircunsferencia + areaRectangulo
        return resultado
    
    
    
circulo = circunsferencia(5)
largo = rectangulo(5,10)
lata = cilindro(circulo, largo)

print(f"Area de la circunsferencia: {circulo.area()}")
print(f"Perimetro de la circunsferencia: {circulo.longitud()}")
print(f"Area del rectangulo: {largo.area()}")
print(f"Area del cilindro: {lata.area()}")