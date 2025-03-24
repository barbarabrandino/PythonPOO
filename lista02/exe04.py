#exercício 4: Atributos de Classe
#Tarefa: Crie uma classe Animal com um atributo de classe categoria. Modifique esse atributo na classe e observe como ele afeta todas as instâncias.
#Objetivo: Entender o comportamento de atributos de classe e sua modificação.

class animal:
    categoria= "animal terrestre"

    def __init__(self, nome):
        self.nome= nome
    
        
animal1= animal("Leão")
animal2= animal("Gato")

print(animal1.categoria)
print(animal2.categoria)

animal.categoria= "mamifero"

print(animal1.categoria)
print(animal2.categoria)



        