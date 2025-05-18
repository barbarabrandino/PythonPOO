class Produto:
    def __init__(self,nome,preco):
        self.nome= nome
        try:
            self.preco = float(preco)
            if self.preco < 0:
                raise ValueError("O preço não pode ser negativo.")
        except ValueError:
            raise ValueError(f"Você não digitou um preço válido para o produto {self.nome}")

        print(f"Produto {self.nome} cadastrado com sucesso!")


        
try:  
        p1= Produto("Arroz", 12)
        print("-------")
        p2=Produto("Feijão", "vinte")
        print("-------")
        p1.validar_preco()
        p2.validar_preco()
except ValueError as erro:
        print(erro)



          
