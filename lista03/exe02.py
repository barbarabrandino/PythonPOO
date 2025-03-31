#Tarefa: Implemente uma classe Carro com um atributo protegido _modelo e um método atualizar_modelo(modelo) para alterar seu valor.

class Carro:
    def __init__(self,modelo):
        self._modelo= modelo

    def mostrar_info(self):
        return f"Modelo do carro:{self._modelo}"

    def atualizar_modelo(self,novo_modelo):
        self._modelo = novo_modelo 
    
carro= Carro("Fusca")
print(carro._modelo)
carro.atualizar_modelo("BMW")
print(carro.mostrar_info())
