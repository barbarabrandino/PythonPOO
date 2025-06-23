#crie uma superclasse FormaGeometrica com um método calcular_area(). Crie subclasses Quadrado e Circulo.

import math

class FormaGeometrica:
    def __init__(self, nome):
        self.nome = nome

    def calcular_area(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")



class Quadrado(FormaGeometrica):
    def __init__(self, nome, lado):
        super().__init__(nome)
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado



class Circulo(FormaGeometrica):
    def __init__(self, nome, raio):
        super().__init__(nome)
        self.raio = raio

    def calcular_area(self):
        return math.pi * (self.raio ** 2)



formas = [
    Quadrado("Quadrado", 4),
    Circulo("Círculo", 3)
]


for forma in formas:
    print(f"{forma.nome} - Área: {forma.calcular_area():.2f}")
