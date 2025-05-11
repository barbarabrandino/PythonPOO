#Desenvolva uma classe Reserva que possui um atributo protegido _detalhes, com método mostrar_detalhes() que exibe as informações.

class Reserva:
    def __init__(self, detalhes):
        self._detalhes = detalhes  

    def mostrar_detalhes(self):
        return self._detalhes 


a1 = Reserva("Informações sobre o produto...")

print(a1.mostrar_detalhes())  
