# Crie um sistema de streaming com as classes Filme e Musica, ambas com o método reproduzir().

class Streaming:
    def __init__(self,nome):
        self.nome = nome 
    def reproduzir(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")
    
class Filme(Streaming):
    def __init__(self, nome):
        super().__init__(nome)
    def reproduzir(self):
        print(f"Reprodizindo Filme: {self.nome}")

class Musica(Streaming):
    def __init__(self, nome):
        super().__init__(nome)
    def reproduzir(self):
        print(f"Reproduzindo a música: {self.nome}")

sistema = [Filme("Lagoa Azul"), Musica("Boate Azul")]

for Streaming in sistema:
    Streaming.reproduzir()