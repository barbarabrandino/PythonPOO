#Crie uma classe Pessoa com o atributo idade. Adicione um método de instância verificar_maioridade() que verifica se a pessoa é maior de idade.

class Pessoa:
    def __init__(self,idade,nome):
        self.nome= nome
        self.idade= idade
    def verificar_maioridade(self):
        if self.idade > 18:
            print("Maior de idade.")
        else:
            print("Menor de idade.")

p1= Pessoa("Julia", 12)
p2= Pessoa("Carlos",22)

p1.verificar_maioridade()
p2.verificar_maioridade()