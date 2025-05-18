class Aluno:
    def __init__(self,nome,nota):
        self.nota = nota
        self.nome = nome
    def validade_nota(self):
        if self.nota < 0 or self.nota >10:
            raise ValueError(f"nota do aluno(a) {self.nome} não é valida")
        print(f"Nota cadastrada com sucesso! Nome do Aluno {self.nome} Nota: {self.nota}")
        
try:
        aluno1=Aluno("Julia", 10)
        aluno1.validade_nota()
        aluno2=Aluno("Carlos", -1)
        aluno2.validade_nota()
except ValueError as error:
        print(error)