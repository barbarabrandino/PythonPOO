# Crie uma classe Loja que mantém um atributo protegido _estoque e um método adicionar_produto(produto) para modificar o estoque

class Loja:
    def __init__(self):
        self._estoque = []

    def adicionar_produto(self,produto):
        self._estoque.append(produto)
    def mostar_estoque(self):
        return self._estoque
    
loja1 = Loja()

loja1.adicionar_produto("Camisa")
loja1.adicionar_produto("Calça")

print(loja1.mostar_estoque())
