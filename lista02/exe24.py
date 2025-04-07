#Tarefa: Crie uma classe Venda com um método estático calcular_imposto(valor) que retorna o valor do imposto sobre o valor passado.

class Venda:
    @staticmethod
    def calcular_imposto(valor):
        return valor * 0.10
valor = 250
imposto = Venda.calcular_imposto(valor)
print(f"Imposto sobre R${valor} é R${imposto:.2f}")