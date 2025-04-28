#Crie uma classe ContaBancaria com um atributo de classe taxa_juros e um método estático calcular_juros(saldo) que calcula os juros sobre o saldo da conta.

class ContaBancaria:
 taxa_juros= 0.05
 @staticmethod
 def calcular_juros(saldo):
    return saldo * ContaBancaria.taxa_juros
saldo_titular = 30200
juros= ContaBancaria.calcular_juros(saldo_titular)
print(f"Juros sobre R$ {saldo_titular}: R$ {juros:.2f}")




















