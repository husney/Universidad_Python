from Monitor import Monitor
from Teclado import Teclado
from Mouse import Mouse
from TiposEntrada import TiposEntrada

class Computadora:
    
    """Crea objetos de tipo Computadora"""
    
    contadorComputadoras = 0
    
    def __init__(self, nombre, monitor, teclado, mouse):
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__mouse = mouse
        Computadora.contadorComputadoras += 1
        self.__idComputador = Computadora.contadorComputadoras
        
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getMonitor(self):
        return self.__monitor
    
    def setMonitor(self, monitor):
        self.__monitor = monitor
        
    def getTeclado(self):
        return self.__teclado
    
    def setTeclado(self, teclado):
        self.__teclado = teclado
        
    def getMouse(self):
        return self.__mouse
    
    def setMouse(self, mouse):
        self.__mouse = mouse
        
    def getIdComputador(self):
        return self.__idComputador
        
    def __str__(self):
        return f"____Computador____\n\nNombre: {self.__nombre}\nID Computador: {self.__idComputador}\n\nMonitor: \n{self.__monitor}\nTeclado: \n{self.__teclado}\nMouse: \n{self.__mouse}__________________\n"
