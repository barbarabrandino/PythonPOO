

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    @classmethod
    def alterar_nome(cls, lista_alunos, novo_nome):
        for aluno in lista_alunos:
            aluno.nome = novo_nome

a1=Aluno("Julia",9.3)
a2=Aluno("Henrique", 10)

alunos = [a1, a2]

for aluno in alunos:
    print(aluno.nome)

Aluno.alterar_nome(alunos, "Bárbara")

for aluno in alunos:
    print(aluno.nome)
