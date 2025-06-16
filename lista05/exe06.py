#Crie SerVivo, Animal, Passaro com métodos de identificação.
class SerVivo:
    def identificar(self):
        return "Sou um ser vivo"

class Animal(SerVivo):
    def identificar(self):
        return "Sou um animal"

class Passaro(Animal):
    def identificar(self):
        return "Sou um pássaro"

print(SerVivo().identificar())
print(Animal().identificar())  
print(Passaro().identificar())  