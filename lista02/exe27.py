#Crie uma classe Produto com os atributos nome e preco. Adicione um método de instância mostrar_info() que retorna uma string com os dados do produto.

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    def mostar_info(self):
        return f"Infos do Produto: {self.nome} - R$ {self.preco}"

p1= Produto("Celular",2300)
p2= Produto("Fone", 230)

p1.mostar_info()
p2.mostar_info()
