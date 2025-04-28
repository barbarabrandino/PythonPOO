#Tarefa: Crie uma classe Funcionario que encapsule o atributo privado __salario e tenha um método informar_salario() que retorna o valor.

class Funcionario:
    def __init__(self,nome,salario):
        self.nome= nome
        self.__salario= salario
    def informar_salario(self):
        return self.__salario
f1= Funcionario("Julia",1200)
print(f1.nome)
print(f1.informar_salario())
