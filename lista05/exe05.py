#Crie Pessoa com nome e idade. Crie Aluno que herda de Pessoa, adicionando matricula.

class Pessoa:
    def __init__(self,nome,idade):
        self.nome= nome
        self.idade= idade
class Aluno(Pessoa):
    def __init__(self, nome, idade,matricula):
        super().__init__(nome, idade)
        self.matricula= matricula
    def detalhes(self):
        print(f"O(A) Aluno(a) {self.nome} de {self.idade} anos: Matricula {self.matricula}")
a1=Aluno("Julia Alvarenga", 12,1005673)
a2=Aluno("Bruno Baldini",16,10065251)

a1.detalhes()
a2.detalhes()