#arefa: Crie uma classe Conta com o atributo saldo e o método verificar_saldo(), que retorna uma mensagem diferente dependendo do valor do saldo.

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def verificar_saldo(self):
        if self.saldo >= 200:
            return "Valor acima de 200 reais!"
        else:
            return "Valor abaixo de 200 reais!"

conta1 = Conta("Ana", 150)
print(conta1.verificar_saldo())  

conta2 = Conta("Luiza", 300)
print(conta2.verificar_saldo())

    
    