#Crie Funcionario com nome, salario. Crie Programador que usa super() e adiciona linguagem.

class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
class Programador(Funcionario):
    def __init__(self, nome, salario,linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem 
    def mostrar(self):
        print(f"Funcionário: {self.nome}\nSalário: R${self.salario}\nLinguagem: {self.linguagem}")
f1= Programador("Ana","6500","Python")
f1.mostrar()
    