#Crie Personagem com vida e forca. Crie Guerreiro e Mago, cada um com habilidade própria.

class Personagem:
    def __init__(self, vida, forca):
        self.vida = vida
        self.forca = forca

class Guerreiro(Personagem):
    def habilidade(self):
        return "Ataque com espada"

class Mago(Personagem):
    def habilidade(self):
        return "Ataque com magia"

guerreiro = Guerreiro(vida=100, forca=50)
mago = Mago(vida=80, forca=70)

print(f"Guerreiro: {guerreiro.habilidade()}")
print(f"Mago: {mago.habilidade()}")

