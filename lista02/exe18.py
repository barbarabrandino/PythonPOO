#Tarefa: Crie uma classe Funcionario com um método salario() e uma classe Gerente que herda de Funcionario e sobrescreve o método salario() para retornar um valor maior.

class Funcionario:
    def __init__(self, nome, salario_inicial):
        self.nome = nome
        self.salario_inicial = salario_inicial

    def salario(self):
        return self.salario_inicial


class Gerente(Funcionario):
    def __init__(self, nome, salario_inicial, bonus):
        self.nome = nome
        self.salario_inicial = salario_inicial
        self.bonus = bonus

    def salario(self):
        return self.salario_inicial + self.bonus


funcionario = Funcionario("João", 3000)
gerente = Gerente("Maria", 3000, 1500)

print(f"Salário do funcionário {funcionario.nome}: R$ {funcionario.salario()}")
print(f"Salário do gerente {gerente.nome}: R$ {gerente.salario()}")
