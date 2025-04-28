#Tarefa: Crie uma classe Produto com um atributo de classe desconto e um método estático aplicar_desconto(preco) que aplica o desconto no preço do produto.

class Produto:
    desconto= 0
    def __init__(self,preco,nome):
        self.perco= preco
        self.nome= nome
    def exibir(self):
        print(f"Nome do Produto: {self.nome} - R${self.preco}")
    @classmethod
    def desconto(cls,novo_valor):
        cls.desconto = novo_valor
    @staticmethod
    def aplicar_desconto(valor):
        return valor - Produto.desconto
    def aplicar (self):
        self.preco= Produto.aplicar_desconto(self.perco)
    
    
p1= Produto("Celular",2000)
p2= Produto("Fone",120)

Produto.aplicar_desconto()

p1.aplicar()
p2.aplicar()

p1.exibir()
p2.exibir()
