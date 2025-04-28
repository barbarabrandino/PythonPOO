#Desenvolva uma classe ContaBancaria com um atributo privado __senha e métodos acessores para acessar o saldo e realizar operações.

import hashlib

class ContaBancaria:
    def __init__(self,senha, titular):
        self.senha= self.__senha(senha)
        self.titular= titular
    def __senha(self,senha):
        return hashlib.sha256(senha.encode()).hexdigest
    def validar_senha(self,senha):
        return self.__senha ==self.senha 

c1= ContaBancaria("Amanda", "senha19201")
print(c1.validar_senha("senha19201"))
print(c1.validar_senha("senha123"))
