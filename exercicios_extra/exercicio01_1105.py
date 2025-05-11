class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Faltava atribuir valor

    def depositar(self, valor):  # Corrigir nome do método e adicionar self
        if valor > 100:
            self.__saldo += valor
            print("Depósito realizado!")
        else:
            print("Depósito insuficiente!")

    def __taxa_bancaria(self):  # Método privado
        return 5

    def consultar_saldo(self):
        return self.__saldo - self.__taxa_bancaria()
