#  Tarefa: Crie uma classe Pessoa com o método de classe criar_pessoa(nome, idade) que cria e retorna uma instância de Pessoa.
#Objetivo: Demonstrar como métodos de classe podem ser usados para criar instâncias.

class pessoa:
    def __init__(self,nome,idade):
        self.nome= nome
        self.idade=idade 
     
    @classmethod
    def criar_pessoa (cls):
           