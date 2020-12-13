class Persona:
    
    __nombre = str
    __apellido = str
    
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getApellido(self):
        return self.__apellido
    
    def setApellido(self, apellido):
        self.__apellido = apellido
        

Sara = Persona("Sara", "Orrego")
print(Sara.getNombre())
print(Sara.getApellido())

 