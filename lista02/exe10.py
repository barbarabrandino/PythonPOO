N#  Tarefa: Crie uma classe Pessoa com o método de classe criar_pessoa(nome, idade) que cria e retorna uma instância de Pessoa.
#Objetivo: Demonstrar como métodos de classe podem ser usados para criar instâncias.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    @classmethod
    def criar_pessoa(cls, nome, idade):
        return cls(nome, idade)
    
pessoa1 = Pessoa("Carlos", 49)
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")

