#Crie uma classe ContaBancaria com o atributo saldo e o método saque(valor). O saque só deve ser realizado se o valor for menor que o saldo.

class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo= saldo 
    def saque(self,valor):
        if valor <= self.saldo:
            valor -= self.saldo
            print(f"Saque de {self.titular} realizado com sucesso!")
        else:
            print(f"Saque de {self.titular} não realizado: valor maior que o saldo disponível!")

t1= ContaBancaria("Carlos",2300)
t2= ContaBancaria ("Julia",1200)

t1.saque(200)
t2.saque(1300)
