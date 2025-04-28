#Tarefa: Implemente uma classe Livro com atributos públicos titulo e autor, e um atributo privado __isbn com um método get_isbn() para acesso.

class Livro:
    def __init__(self,titulo,autor,isbn):
        self.titulo = titulo
        self.autor = autor
        self.__isbn = isbn
    def get_isbn(self):
        return self.__isbn
l1= Livro("Jantar Secreto", "Rapahel Montes", 1288392832)
print(l1.titulo, l1.autor, l1.get_isbn())

