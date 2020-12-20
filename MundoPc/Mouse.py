from DispositivoEntrada import DispositivoEntrada
from TiposEntrada import TiposEntrada

class Mouse(DispositivoEntrada):
    
    """Crea un objeto de tipo Mouse"""
        
    contadorRatones = 0
    
    def __init__(self, tipoEntrada, marca):
        DispositivoEntrada.__init__(self, tipoEntrada, marca)
        Mouse.contadorRatones += 1
        self.__idMouse = Mouse.contadorRatones
        
    def getIdMouse(self):
        return self.__idMouse
        
    def __str__(self):
        return f"ID Mouse: {self.__idMouse}\n" + DispositivoEntrada.__str__(self) 
    
    