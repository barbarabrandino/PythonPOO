#Tarefa: Crie uma classe Calculadora com um método estático somar(a, b) que retorna a soma de dois números.
#Objetivo: Entender como os métodos estáticos não precisam de instância e são utilizados para funcionalidades utilitárias.

class Calculadora:
    def somar(a,b):
        return a + b

resultado1= Calculadora.somar(30,50)

resultado2= Calculadora.somar(40,60)

print(f"O resultado de 30 + 50 = {resultado1}")
print(f"O resultado da 40 + 60 = {resultado2}")

