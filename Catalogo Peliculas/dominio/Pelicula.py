class Pelicula:
    """Representa un objeto película"""
    
    def __init__(self, nombre, categoria):
        self.__nombre = nombre
        self.__categoria = categoria
        
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getCategoria(self):
        return self.__categoria

    def setCategoria(self, categoria):
        self.__categoria =  categoria
    
    def __str__(self):
        return f"---PELICULA---\n Nombre: {self.__nombre}\n Categoria: {self.__categoria}\n--------------\n"