class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def mostrar_detalhes(self):  
        print(f"{self.nome} ganha R${self.salario:.2f} | Departamento: {self.departamento}")


f1 = Gerente("Ana Gonçalves", 15500.89, "Logistica")
f2 = Gerente("Bernardo Vilela", 15400.90, "TI")


f1.mostrar_detalhes()
f2.mostrar_detalhes()
