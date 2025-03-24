class produto:
    def __init__(self, preco,nome):
        self.nome = nome
        self.preco = preco
    def exibir (self):
        
        print(f"Nome:{produto01.nome}, Preço:{produto01.preco}")

produto01= produto ("Cacau", 56)
produto.exibir()


produto01.preco= 12
produto.exibir()

