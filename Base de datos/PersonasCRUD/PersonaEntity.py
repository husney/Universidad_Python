from logBase import logger
class Persona:
    
    
    __personas = 0
    
    def __init__(self, nombre, apellido, email):
        Persona.__personas -= 1 
        self.__id = Persona.__personas
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
    
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getApellido(self):
        return self.__apellido
    
    def setApellido(self, apellido):
        self.__apellido = apellido
    
    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email
        
    def __str__(self):
        return f"\nId: {self.__id}\nNombre: {self.__nombre}\nApelido: {self.__apellido}\nEmail: {self.__email}\n"
    
    
        
        


