#Tarefa: Crie uma classe ContaBancaria com os atributos titular e saldo. Adicione um método de instância depositar(valor) que aumenta o saldo da conta.
#Objetivo: Demonstrar como modificar atributos de instância usando métodos.

class ContaBancaria:
    def __init__(self,titular, saldo_inicial=0):
        self.titular = titular
        self.saldo= saldo_inicial
    def depositar( self,valor): 
        if valor  > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor} realizado com sucesso!")
        else:
            print("O valor do depósito deve ser positivo.")

    def consultar_saldo (self):
        print(f"Saldo da conta do {self.titular} é de R${self.saldo}")

    def consultar_saldo(self):
        print(f"O saldo final da conta do titular {self.titular} é de R${self.saldo}")
    
conta1= ContaBancaria ("Pedro", 2300)
conta1.consultar_saldo()

conta1.depositar(3000)
conta1.consultar_saldo()
