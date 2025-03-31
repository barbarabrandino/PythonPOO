#Crie uma classe ContaBancaria com o atributo privado __saldo e um método depositar(valor) que aumenta o saldo.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

    def exibir_saldo(self):
        print(f"Saldo atual de {self.titular}: R$ {self.__saldo:.2f}")

conta1 = ContaBancaria("Alice", 2040.63)
conta1.exibir_saldo()

conta1.depositar(5000.90)
conta1.exibir_saldo()
