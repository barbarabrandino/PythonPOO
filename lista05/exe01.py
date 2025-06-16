class Animal:
    def falar(self):
        return"Som Qualquer"
    
class Cachorro(Animal):
    def falar(self):
        return "AU AU"
    
class Gato(Animal):
    def falar(self):
        return "Miau"

print(Cachorro().falar())
print(Gato().falar())