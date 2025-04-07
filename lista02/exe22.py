#Tarefa: Crie uma classe Pessoa com um atributo de classe total_pessoas. Cada vez que uma nova instância for criada, o total_pessoas deve ser incrementado. Teste a alteração com várias instâncias.
class Pessoa:
    total_pessoas = 0  

    def __init__(self, nome):
        self.nome = nome
        Pessoa.total_pessoas += 1

    @classmethod
    def exibir_total(cls):
        print(f"Total de pessoas: {cls.total_pessoas}")


p1 = Pessoa("Ana")
p2 = Pessoa("Carlos")
p3 = Pessoa("Beatriz")


Pessoa.exibir_total()
