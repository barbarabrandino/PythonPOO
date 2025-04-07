#Tarefa: Crie uma classe Curso com o atributo de instância nome e o atributo de classe quantidade_cursos. Adicione um método de classe alterar_quantidade_cursos() que modifica o valor de quantidade_cursos.
 
class Curso:
    quantidade_cursos = 0 

    def __init__(self, nome):
        self.nome = nome

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"A quantidade total de cursos é: {Curso.quantidade_cursos}")

    @classmethod
    def alterar_quantidade_cursos(cls, nova_quantidade):
        cls.quantidade_cursos = nova_quantidade



curso01 = Curso("Teatro")


curso01.exibir()


Curso.alterar_quantidade_cursos(5)


curso01.exibir()

