#Tarefa: Crie uma classe Pessoa com um atributo público idade e um método validar_idade(), que retorna True se a idade for maior ou igual a 18.

class Pessoa:
    def __init__(self,idade,nome):
        self.nome = nome 
        self.idade = idade
    def validar_idade(self):
        if self.idade >= 18:
            return True
        else:
            return False
        
p1= Pessoa("Julia", 18)
p2= Pessoa("Ana", 13)

print(p1.validar_idade())
print(p2.validar_idade())
    
