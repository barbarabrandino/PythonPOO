

import hashlib

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.__senha = self.__criptografar_senha(senha) 

    def __criptografar_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()  

    def validar_senha(self, senha):
        return self.__criptografar_senha(senha) == self.__senha

usuario = Usuario("Clarissa", "minha_senha_")
print(usuario.validar_senha("minha_senha_"))  
print(usuario.validar_senha("senhaErrada")) 