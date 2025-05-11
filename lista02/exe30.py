# Crie uma classe Cliente com o atributo nome e um método estático validar_cpf(cpf) que retorna True se o CPF for válido. Use esse método no método de instância cadastrar_cliente().

class Cliente:
    def __init__(self,nome):
        self.nome = nome
    def cadastrar_cliente(self,cpf):
        if Cliente.validar_cpf(cpf):
            self.cpf = cpf
            print(f"\n CPF do cliente {self.nome} é válido! Cadastro realizado com sucesso.")
        else:
            print(f"CPF inválido : {cpf}. Cadastro não realizado.")
    @staticmethod
    def validar_cpf(cpf):
        if len(cpf) != 11:
            return False
        
        if cpf == cpf [0]*11:
            return False
        
        return True
    
c1= Cliente("Ana")
c2= Cliente("Claudio")

c1.cadastrar_cliente("46800954430")
c2.cadastrar_cliente("23467812340")
Cliente.validar_cpf("46800954430")
Cliente.validar_cpf("23467812340")