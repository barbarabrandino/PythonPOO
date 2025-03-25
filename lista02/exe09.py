#Tarefa: Crie uma classe Loja com o atributo de classe desconto. Adicione um método de classe aplicar_desconto() que modifica o valor do desconto para todas as instâncias.
#Objetivo: Demonstrar a alteração de atributos de classe por métodos de classe.

class Loja:
    desconto = 0  

    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco

    def com_desconto(self):
        return self.preco - Loja.desconto  

    def exibir(self):
        print(f"O produto sem desconto: {self.produto} - R$ {self.preco:.2f}")
        print(f"O produto com desconto: {self.produto} - R$ {self.com_desconto():.2f}\n")

    @classmethod
    def aplicar_desconto(cls, valor_desconto):
        cls.desconto = valor_desconto  


produto1 = Loja("Sapatilha", 200)
produto2 = Loja("Saia", 100)
produto3 = Loja("Blusa", 50)

print("Antes de aplicar o desconto:")
produto1.exibir()
produto2.exibir()
produto3.exibir()

Loja.aplicar_desconto(20)

print("Após aplicar o desconto de R$20:")
produto1.exibir()
produto2.exibir()
produto3.exibir()
