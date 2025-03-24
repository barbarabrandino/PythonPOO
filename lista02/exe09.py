#Tarefa: Crie uma classe Loja com o atributo de classe desconto. Adicione um método de classe aplicar_desconto() que modifica o valor do desconto para todas as instâncias.
#Objetivo: Demonstrar a alteração de atributos de classe por métodos de classe.

class loja:
    desconto = 0
    def __init__(self,produto, preco):
        self.produto = produto
        self.preco = preco

    def com_desconto(self):
        return self.produto - loja.desconto
    def exibir(self):
        print(f" O produto sem desconto; \n{self.produto} : R$ {self.preco}")
        print(f"O produto com desconto: \n {self.produto} : R${self.com_desconto}")

    @classmethod
    def aplicar_desconto(cls, com_denscoto):
        cls.desconto = com_denscoto

produto1= loja("Sapatilha", 200)
produto2= loja("Saia", 100)
produto3= loja ("blusa", 50)
 
produto1.exibir()
produto2.exibir()
produto3.exibir()

loja.aplicar_desconto(20)


produto1.exibir()
produto2.exibir()
produto3.exibir()