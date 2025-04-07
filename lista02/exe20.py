#arefa: Crie uma classe Livro com um método de classe criar_livro(titulo, autor) que cria e retorna uma instância de Livro com base nos parâmetros passados.
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")

    @classmethod
    def criar_livro(cls, titulo, autor):
        return cls(titulo, autor)


# Exemplo de uso
livro1 = Livro.criar_livro("1984", "George Orwell")
livro2 = Livro.criar_livro("Dom Casmurro", "Machado de Assis")

livro1.exibir()
livro2.exibir()
