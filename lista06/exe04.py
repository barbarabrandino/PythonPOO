class Passaro:
    def movimentar(self):
        return "Voando pelos céus."

class Peixe:
    def movimentar(self):
        return "Nadando no oceano."
    
animais=[Peixe(),Passaro()]

for animal in animais:
    animais.movimentar()