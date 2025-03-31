#Tarefa: Crie uma classe Aluno com os atributos nome e nota. Crie várias instâncias e modifique os atributos de cada uma de forma independente.

class Aluno:
    def __init__(self,nome="sem nome ",nota= 0):
        self.nome= nome
        self.nota= nota

a= Aluno()
a.nome= "Paulo"
a.nota= 7.5
print(a.nome, a.nota)

a2= Aluno()
a2.nome= "Julia"
a2.nota= 9.5
print(a2.nome, a2.nota)

