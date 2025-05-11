#Crie uma classe Banco com um atributo privado __taxa_juros e um método privado __calcular_juros(saldo).

class Banco:
    def __init__(self, saldo_inicial):
        self.__taxa_juros = 0.05  
        self.saldo = saldo_inicial

    def aplicar_juros(self):
       
        juros = self.__calcular_juros(self.saldo)
        self.saldo += juros
        return juros

    def __calcular_juros(self, saldo):
        
        return saldo * self.__taxa_juros


conta = Banco(1000)


juros_aplicados = conta.aplicar_juros()
print("Juros aplicados:", juros_aplicados)
print("Novo saldo:", conta.saldo)
