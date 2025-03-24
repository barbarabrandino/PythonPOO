#Tarefa: Crie uma classe Funcionario com o atributo de classe bonus. Adicione um método de classe modificar_bonus(valor) que altera o valor do bônus.
#Objetivo: Compreender como os métodos de classe operam sobre atributos de classe.

class Funcionario:
    bonus= 600
    def __init__(self,nome, salario):
        self.nome = nome
        self.salario = salario
    def antes_bonus (self):
        return self.salario +  Funcionario.bonus
    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Salário sem bônus: R${self.salario}")
        print(f"Salário com bônus: R${self.antes_bonus():.2f}")

    @classmethod 
    def modificar_bonus (cls,novo_bonus):
        cls.bonus = novo_bonus

    @classmethod 
    def exibir_novo(cls):
        print(f"\nO bônus atualizado é de R${Funcionario.bonus}")

Funcionario1 = Funcionario("Eduardo", 3000)
Funcionario2= Funcionario("Helena", 4000)
Funcionario1.exibir()
Funcionario2.exibir()

Funcionario.modificar_bonus(1000)

Funcionario1.exibir_novo()
Funcionario1.exibir()
Funcionario2.exibir()
Funcionario2.exibir_novo()