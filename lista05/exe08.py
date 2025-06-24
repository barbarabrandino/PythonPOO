#Crie Conta com saldo, depositar e sacar. Crie ContaCorrente com limite e sobrescreva sacar.
class Conta:
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso."
        else:
            return "Saque maior que o saldo. Saque não realizado."


class ContaCorrente(Conta):
    def __init__(self, saldo, limite):
        super().__init__(saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com uso do limite."
        else:
            return "Saque maior que saldo + limite. Saque não realizado."



conta_simples = Conta(500)
print(conta_simples.sacar(600))  
print(conta_simples.sacar(400)) 

conta_corrente = ContaCorrente(500, 300)
print(conta_corrente.sacar(700))  
print(conta_corrente.sacar(900))  

