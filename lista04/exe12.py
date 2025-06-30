class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def verificar_maioridade(self):
        try:
            idade_inteira = int(self.idade)
            if idade_inteira >= 18:
                return f"{self.nome} é maior de idade."
            else:
                return f"{self.nome} é menor de idade."
        except ValueError:
            return f"Erro: A idade de {self.nome} deve ser um número inteiro."
