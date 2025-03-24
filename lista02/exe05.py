#Tarefa: Crie uma classe Pessoa com os atributos nome e idade. Adicione um método de instância apresentar() que retorna uma string com o nome e a idade da pessoa.
#Objetivo: Compreender como os métodos de instância operam sobre os atributos do objeto.

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar (self):
        return(f"Meu nome é {self.nome} e tenho {self.idade} anos!")
    
pessoa1= pessoa("Bruna", 24)
print(pessoa1.apresentar())
