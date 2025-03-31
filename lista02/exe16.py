#Tarefa: Crie uma classe Carro com os atributos modelo e cor. Defina valores padrão para esses atributos caso não sejam passados durante a criação da instância.

class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor

    def exibir_padrão(self):
        return f"Modelo do carro é : {self.modelo} : {self.cor}"
        
carro01= Carro()
carro02 = Carro("BMW", "Preto")

print (carro01.modelo, carro01.cor)
print( carro02.modelo, carro02.cor) 