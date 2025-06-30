class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} {self.modelo}"


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int):
        super().__init__(marca, modelo)
        if not isinstance(portas, int) or portas <= 0:
            raise ValueError("O número de portas deve ser um inteiro maior que zero.")
        self.portas = portas

    def __str__(self):
        return f"{super().__str__()} - {self.portas} portas"
