class Usuario:

    USUARIOS = 0

    def __init__(self, nombre, password):
        Usuario.USUARIOS -= 1
        self.__id = Usuario.USUARIOS
        self.__nombre = nombre
        self.__password = password

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def __str__(self):
        return f"Id: {self.__id}\nNombre: {self.__nombre}\nPassword: {self.__password}\n"


