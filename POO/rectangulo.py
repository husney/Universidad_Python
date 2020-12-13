class Rectangulo:
    
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
        
    def calcularArea(self):
        return self.__base * self.__altura
    
    
base = int(input("Por favor ingrese la base del triangulo: "))
altura = int(input("Por favor ingrese la altura del triangulo: "))
rectangulo1 = Rectangulo(base, altura)
print("El area del triangulo es:",rectangulo1.calcularArea())