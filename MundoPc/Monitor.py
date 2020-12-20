from DispositivoEntrada import DispositivoEntrada
from TiposEntrada import TiposEntrada


class Monitor(DispositivoEntrada):
    
    """Crea objetos de tipo monitor"""
    
    contadorMonitores = 0
    
    def __init__(self, tipoEntrada, marca, diametro):
        DispositivoEntrada.__init__(self, tipoEntrada, marca)
        self.__diametro = diametro
        Monitor.contadorMonitores += 1
        self.__idMonitor = Monitor.contadorMonitores
    
    def getDiametro(self):
        return self.__diametro
    
    def setDiametro(self, diametro):
        self.__diametro = diametro
        
    def getIdMonitor(self):
        return self.__idMonitor
        
    def __str__(self):
        return f"ID Monitor: {self.__idMonitor}\n" + DispositivoEntrada.__str__(self) + f"Tamaño: {self.__diametro}\n"