#Implemente uma classe Produto onde o atributo privado __preco pode ser acessado através de um método público get_preco().

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco 
    def get_preco(self):
        return self.__preco
p1= Produto("Celular", 6539.67)
print(f"Produto: {p1.nome}")
print(f"Preço: R${p1.get_preco():.2f}")
