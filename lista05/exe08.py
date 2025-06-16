#Crie Conta com saldo, depositar e sacar. Crie ContaCorrente com limite e sobrescreva sacar.
class Conta:
    def __init__(self,saldo):
        self.saldo =  saldo
    def depositar(self,valor):
        self.saldo += valor
    def sacar(self,valor):
        if self.valor <= self.saldo:
            return f"Saque de R${self.valor} foi realizado com sucesso"
        else:
            return "Saque maior que valor do saldo.\nSaque não realizado."
class ContaCorrente(Conta):
    def __init__(self, saldo,limite):
        super().__init__(saldo)
        self.limite = limite
    def sacar(self,valor):
        if self.valor <= self.saldo + self.limite:
            self.saldo -= valor
            return True
        else:
            False


