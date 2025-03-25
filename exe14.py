# Crie uma classe Banco com um atributo de classe taxa_juros. Adicione um método estático calcular_juros(saldo) que calcula os juros sobre um saldo, considerando a taxa de juros da classe

class Banco:
    taxa_juros= 0.05
    @staticmethod
    def calcular_juros(saldo):
        return saldo * Banco.taxa_juros
    
saldo_titular = 2000
juros= Banco.calcular_juros(saldo_titular)
print(f"Juros sobre R$ {saldo_titular}: R$ {juros:.2f}")