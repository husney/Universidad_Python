class Caja:
    
    def __init__(self, alto, ancho, largo):
        self.__alto = alto
        self.__ancho = ancho
        self.__largo = largo
    
    def calcularVolumnen(self):
        return self.__alto * self.__ancho * self.__largo
    
    
alto = int(input("Por favor inrese el alto de la caja: "))
ancho = int(input("Por favor ingrese el ancho de la caja: "))
largo = int(input("Por favor ingrese el largo de la caja: "))
caja1 = Caja(alto, ancho, largo)
print(caja1.calcularVolumnen(), "M^3")


