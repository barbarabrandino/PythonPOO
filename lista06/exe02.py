#Crie uma superclasse Funcionario com um método calcular_salario(). Crie duas subclasses: FuncionarioCLT e FuncionarioPJ. Cada uma calcula o salário de forma diferente.

class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return 0

class FuncionarioCLT(Funcionario):
    def calcular_salario(self):
        return self.salario_base - (self.salario_base * 0.1) 
    
class FuncionarioPJ(Funcionario):
    def calcular_salario(self):
        return self.salario_base 
    