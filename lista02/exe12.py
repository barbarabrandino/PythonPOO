#Tarefa: Crie uma classe Pessoa com um método estático validar_idade(idade) que retorna True se a idade for maior ou igual a 18 e False caso contrário.
#Objetivo: Demonstrar como métodos estáticos podem ser usados para validações sem depender de instância.

class Pessoa:
    @staticmethod
    def validar_idade(idade):
        return idade >= 18  

idade = int(input("Digite sua idade: "))

if Pessoa.validar_idade(idade):
    print("Idade validada!")
else:
    print("Menor de idade! Não validada.")

