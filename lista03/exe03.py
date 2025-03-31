#Desenvolva uma classe ContaBancaria com um atributo privado __senha e métodos acessores para acessar o saldo e realizar operações.

import hashlib

class ContaBancaria:
    def __init__(self,__senha, titular):
        self.__senha= __senha
        self.titular= titular

    