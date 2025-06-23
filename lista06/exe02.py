#Crie uma superclasse Funcionario com um método calcular_salario(). Crie duas subclasses: FuncionarioCLT e FuncionarioPJ. Cada uma calcula o salário de forma diferente.
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def calcular_salario(self):
        raise NotImplementedError("Este método deve ser implementado nas subclasses.")



class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.salario_mensal



class FuncionarioPJ(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario(self):
        return self.valor_hora * self.horas_trabalhadas



funcionarios = [
    FuncionarioCLT("João", 5000),
    FuncionarioPJ("Maria", 100, 100),
    FuncionarioPJ("Carlos", 150, 80),
    FuncionarioCLT("Ana", 6200)
]

for funcionario in funcionarios:
    print(f"{funcionario.nome} - Salário: R${funcionario.calcular_salario():.2f}")

