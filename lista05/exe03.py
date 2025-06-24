class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

    def abrir_porta_malas(self):
        return "Porta-malas aberto"

class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

    def empinar(self):
        return "Moto empinando!"
    

carro1 = Carro("Toyota", 2022, 4)
moto1 = Moto("Honda", 2021, 250)

print(f"Carro: {carro1.marca}, Ano: {carro1.ano}, Portas: {carro1.portas}")
print(carro1.abrir_porta_malas())

print(f"Moto: {moto1.marca}, Ano: {moto1.ano}, Cilindradas: {moto1.cilindradas}")
print(moto1.empinar())
