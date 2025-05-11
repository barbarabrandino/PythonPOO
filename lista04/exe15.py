class ProdutoNaoEncontrado(Exception):
    pass

class Loja:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto):
        self.produtos.append(produto)
    
    def remover_produto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
        else:
            raise ProdutoNaoEncontrado(f"Produto '{produto}' não encontrado.")
    
    def listar_produtos(self):
        return self.produtos


loja = Loja()
loja.adicionar_produto("Camiseta")
loja.adicionar_produto("Calça Jeans")
print(loja.listar_produtos())

try:
    loja.remover_produto("Tênis")
except ProdutoNaoEncontrado as e:
    print(e)

loja.remover_produto("Camiseta")
print(loja.listar_produtos())
