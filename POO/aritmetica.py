
class Aritmetica:
    
    def __init__(self, n1, n2):
        self.__n1 = n1
        self.__n2 = n2
        
    def sumar(self):
        return self.__n1 + self.__n2
    
    def restar(self):
        return self.__n1 - self.__n2

    def multiplicar(self):
        return self.__n1 * self.__n2
    
    def dividir(self):
        return self.__n1 / self.__n2
    
    def __str__(self):
        return ("Objeto Aritmetico")
    

mat = Aritmetica(5,10)

print(mat.sumar())
    
    