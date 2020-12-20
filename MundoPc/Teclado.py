from DispositivoEntrada import DispositivoEntrada
from TiposEntrada import TiposEntrada

class Teclado(DispositivoEntrada):
    
    """Crea objetos de tipo Teclado"""
    
    contadorTeclados = 0
    
    def __init__(self, tipoEntrada, marca, tipo):
        DispositivoEntrada.__init__(self, tipoEntrada, marca)
        Teclado.contadorTeclados += 1
        self.__idTeclado = Teclado.contadorTeclados
        self.__tipo = tipo
        
    def getIdTeclado(self):
        return self.__idTeclado

    def getTipo(self):
        return self.__tipo
    
    def setTipo(self, tipo):
        self.__tipo = tipo
    
    def __str__(self):
        return f"ID Teclado: {self.__idTeclado}\nTipo: {self.__tipo}\n" + DispositivoEntrada.__str__(self) 
        
    