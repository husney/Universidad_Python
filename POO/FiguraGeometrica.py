class FiguraGeometrica:
    
    def __init__(self, alto, ancho):
        self.__alto = alto
        self.__ancho = ancho
    
    def getAlto(self):
        return self.__alto
    
    def setAlto(self, alto):
        self.__alto = alto
        
    def getAncho(self):
        return self.__ancho

    def setAncho(self, ancho):
        self.__ancho = ancho
        
    def __str__(self):
        return f"Alto: {self.__alto}\nAncho: {self.__ancho}"