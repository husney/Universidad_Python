#ABC = Abstract Base Class

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    
    def __init__(self, alto, ancho):
        self.__alto = alto
        self.__ancho = ancho
    
    @abstractmethod
    def area(self):
        pass
    
    def getAlto(self):
        return self.__alto
    
    def setAlto(self, alto):
        self.__alto = alto
        
    def getAncho(self):
        return self.__ancho

    def setAncho(self, ancho):
        self.__ancho = ancho
        
        
    
    

class Color:
    
    def __init__(self, color):
        self.__color = color
    

    
class Cuadrado(FiguraGeometrica, Color):
    
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
        
    def area(self):
        return FiguraGeometrica.getAncho(self) * FiguraGeometrica.getAlto(self)
    
    
    
c = Cuadrado(10,4,"Morado")

print(c.area())
        


class Rectangulo(FiguraGeometrica, Color):
    
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
        
    def area(self):
        return FiguraGeometrica.getAlto(self) * FiguraGeometrica.getAncho(self)
    

r = Rectangulo(5,3, "Azul")
print(r.area())