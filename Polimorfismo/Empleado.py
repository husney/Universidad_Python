class Empleado:
    
    def __init__(self, nombre, sueldo):
        self.__nombre = nombre
        self.__sueldo = sueldo


    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getSueldo(self):
        return self.__sueldo

    def setSueldo(self, sueldo):
        self.__sueldo = sueldo

    def __str__(self):
        return f"Nombre: {self.__nombre}\nSueldo: {self.__sueldo}"