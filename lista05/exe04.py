import math

class Forma:
    def calcular_area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

q = Quadrado(6)
c = Circulo(8)


print(f"Área do quadrado: {q.calcular_area():.2f}")
print(f"Área do círculo: {c.calcular_area():.2f}")
