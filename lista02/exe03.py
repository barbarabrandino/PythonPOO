class produto:
    def __init__(self, preco,nome):
        self.nome = nome
        self.preco = preco

produto01= produto ("Cacau", 56)

produto01.preco= 12

print(f"Nome:{produto01.nome}, Preço:{produto01.preco}")