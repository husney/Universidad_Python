from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)


    def area(self):
        return FiguraGeometrica.getAlto(self) * FiguraGeometrica.getAncho(self)
    
    
    def getAlto(self):
        print(FiguraGeometrica.getAlto(self))
      
    def __str__(self):
        return FiguraGeometrica.__str__(self) + f"\nColor: {Color.getColor(self)}"
        


class Rectangulo(FiguraGeometrica, Color):
    
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
        
    def area(self):
        return FiguraGeometrica.getAlto(self) * FiguraGeometrica.getAncho(self)
        
    def __str__(self):
        return FiguraGeometrica.__str__(self) + f"\nColor: {Color.getColor(self)}"