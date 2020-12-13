"""class Persona:
    
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre"""
        

        
"""p1 = Persona("Sara")
print(p1.getNombre())

p1.setNombre("Sara Orrego")
print(p1.getNombre())"""


class Persona:
    
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        
    def mostrarDetalles(self):
        self.__metodo_privado()
    
    def __metodo_privado(self):
        print(self.__nombre)
        print(self.__apellido)
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getApellido(self):
        return self.__apellido
  
    def setApellido(self, apellido):
        self.__apellido = apellido
    

p1 = Persona("Sara", "Orrego")
p1.mostrarDetalles()
    
    
    
        

