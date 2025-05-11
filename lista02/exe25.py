#Tarefa: Crie uma classe Produto com um atributo de classe desconto e um método estático aplicar_desconto(preco) que aplica o desconto no preço do produto.

class Produto:
    desconto = 0  # Atributo de classe

    def __init__(self, nome, preco):  # Corrigi a ordem dos parâmetros
        self.nome = nome
        self.preco = preco  # Corrigido de 'perco'

    def exibir(self):
        print(f"Nome do Produto: {self.nome} - R${self.preco:.2f}")

    @classmethod
    def definir_desconto(cls, novo_valor):  # Nome trocado para não conflitar com o atributo
        cls.desconto = novo_valor

    @staticmethod
    def aplicar_desconto(valor):
        return valor - Produto.desconto

    def aplicar(self):
        self.preco = Produto.aplicar_desconto(self.preco)

