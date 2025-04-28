#Crie uma classe Aluno com um atributo protegido _nota e um método protegido modificar_nota(nota) para alterar a nota.

class Aluno:
    def __init__(self,nome,nota):
        self.nome=nome
        self._nota= nota
    def mostrar_notas(self):
        return f"Nome do aulno: {self.nome} - nota: {self._nota}"
    def modificar_nota(self,nova_nota):
        self._nota = nova_nota
    
a1=Aluno("Clara", 9.5)
print(a1._nota)

a1.modificar_nota(10)
print(a1.mostrar_notas())
