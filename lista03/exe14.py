#Tarefa: Crie uma classe Cliente com um atributo privado __cpf, um método cadastrar_cliente() e um método estático validar_cpf(cpf).
class Cliente:
    def __init__(self,nome):
        self.nome = nome
    def cadastrar_cliente(self,cpf):
        if Cliente.validar_cpf(cpf):
            self.__cpf = cpf
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
    def mostrar_cpf(self):
        return self.__cpf

c1= Cliente("Ana")


c1.cadastrar_cliente("46800258830")


print(f"\nCPF de {c1.nome} é {c1.mostrar_cpf()}")
