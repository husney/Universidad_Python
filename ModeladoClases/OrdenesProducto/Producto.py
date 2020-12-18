class Producto:
    
    productos_count = 0
    
    def __init__(self, nombre, precio):
        Producto.productos_count += 1
        self.__idProducto = Producto.productos_count
        self.__nombre = nombre
        self.__precio = float(precio) * 1.16
        
    def getIdProducto(self):
        return self.__idProducto
    
    def setIdProducto(self, idProducto):
        self.__idProducto = int(idProducto)
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, precio):
        self.__precio = float(precio)
        
    def __str__(self):
        return f"_____PRODUCTO_____\nNombre: {self.__nombre}\nID: {self.__idProducto}\nPrecio: {self.__precio}"
    
    