#Tarefa: Crie uma classe Aluno com os atributos nome e nota. Adicione um método de instância situacao() que retorna "Aprovado" se a nota for maior ou igual a 6 e "Reprovado" caso contrário.
#Objetivo: Trabalhar com métodos de instância que utilizam condicionais.

class Aluno:
    def __init__(self,nome, nota):
        self.nome = nome
        self.nota = nota

    def situacao(self): 
        if self.nota >= 6:
         return print(f"Parabéns você foi aprovaodo!  \n Aluno: {self.nome} \n Nota: {self.nota}")
        else:
           return print (f"Você foi reprovado \n Aluno: {self.nome} \n Nota: {self.nota}")
        
aluno1= Aluno ("Julia",7)
aluno2= Aluno("Paulo", 4.5)

aluno1.situacao()
aluno2.situacao()
