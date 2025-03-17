class carro:
    def __init__ (self,modelo,ano):
        self.modelo= modelo
        self.ano=ano 

    def exibir (self):
        print(f"Modelo: {self.modelo}, Ano: {self.ano}")

carro1= carro ("Porche",2024)
carro2= carro("BMW", 2023)

carro1.exibir()
carro2.exibir()