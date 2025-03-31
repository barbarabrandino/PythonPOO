#Tarefa: Crie uma classe Produto com um atributo público nome e um método exibir_nome() que exibe o nome do produto.
 
class Produto:
    def __init__(self, nome, preco):
        self.nome= nome
        self.preco = preco

    def exibir_nome(self):
        return f"Produto: {self.nome}: R${self.preco}"
    
produto1= Produto("Chocolate", 20)

print(produto1.nome)
print(produto1.preco)
