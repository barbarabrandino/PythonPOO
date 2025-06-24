#Crie Professor e Pesquisador. Crie Cientista que herda ambos e usa trabalhar() com os dois comportamentos.

        
class Professor:
    def trabalhar(self):
        return "Dar aula"
        
class Pesquisador:
    def trabalhar(self):
        return "Pesquisa"
    
class Cientista(Professor, Pesquisador):
    def trabalhar(self):
        return super().trabalhar()

c = Cientista()
print(c.trabalhar())


