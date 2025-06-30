class ContaBancaria:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para o saque.")
        self.saldo -= valor

    def __str__(self):
        return f"Conta de {self.titular}, Saldo: R${self.saldo:.2f}"
