class Calculadora:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def dividir(self,a,b):
        if b == 0:
         raise ZeroDivisionError("O valor de b não pode ser zero!")
        resultado= self.a/self.b
        return resultado
        
        try:
            calc1= Calculadora()
            calc1.dividir(10,5)
        except ZeroDivisionError as error:
           print(error)
