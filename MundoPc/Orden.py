from Computadora import Computadora


class Orden:
    
    """Crea objetos de tipo orden y almacena una lista de objetos de tipo Computadora"""
    
    contadorOrdenes = 0
    
    def __init__(self):
        Orden.contadorOrdenes += 1
        self.__idOrden = Orden.contadorOrdenes
        self.__computadoras = []
        
    def agregarComputadora(self, computadora):
        self.__computadoras.append(computadora)
        
    def getComputadoras(self):
        return self.__computadoras
    
    def getIdOrden(self):
        return self.__idOrden
        
    def __str__(self):
        datos = f"Orden { self.__idOrden}\n"
        for computadora in self.__computadoras:
            datos += computadora.__str__()
            
        return datos
    
    