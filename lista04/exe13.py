class ErrorSaldoInsulficiente:
    pass
class ValorNegativo:
    pass



class ContaBancaria:
    def __init__(self,saldo):
        self.saldo= saldo
    
    def saque(self,valor):
        if valor > self.saldo:
            raise ErrorSaldoInsulficiente("Saldo Insulficiente")
        if valor < 0:
            raise ValorNegativo("Valor negativo")
        self.saldo -= valor
        return self.saldo
        try:        
            conta1=ContaBancaria(500)
            print(conta1.saque(100))

            conta2= ContaBancaria(300)
            print(conta2.saque(600))

            conta3=ContaBancaria(400)
            print(conta3.saque(-80))
        except ErrorSaldoInsulficiente as error:
            print(error)
         
        except ValorNegativo as error:
         print(error)