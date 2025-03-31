#Tarefa: Crie uma classe Produto com os atributos nome e preco. Adicione um método aplicar_desconto(desconto) que aplica um desconto ao preço do produto.
class Loja:
    def __init__(self, preco, nome):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, desconto):
        self.preco -= self.preco * desconto 
    def exibir(self):
        print(f"{self.nome}: R$ {self.preco:.2f}") 
produto1 = Loja(2000, "Celular")

produto1.aplicar_desconto(0.05)

produto1.exibir()

