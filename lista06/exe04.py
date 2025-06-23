#Crie um sistema de animais com as classes Passaro e Peixe, ambas com o método movimentar().
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def movimentar(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")


class Passaro(Animal):
    def movimentar(self):
        print(f"O pássaro {self.nome} está voando.")


class Peixe(Animal):
    def movimentar(self):
        print(f"O peixe {self.nome} está nadando.")



animais = [
    Passaro("Arara-azul"),
    Peixe("Baiacu")
]


for animal in animais:
    animal.movimentar()




