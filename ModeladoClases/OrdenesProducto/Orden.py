from Producto import Producto
class Orden:
    
    ordenes_count = 0
    
    def __init__(self, productos):
        Orden.ordenes_count += 1
        self.__id = Orden.ordenes_count
        self.__productos = productos
        
    def getIdOrden(self):
        return self.__idOrden
    
    def setIdOrden(self, idOrden):
        self.__idOrden = int(idOrden)
        
    def getProductos(self):
        return self.__generados
        
    def actualizarProductos(self):
        self.__generados = self.__generadorProductos()
        return self.__generados
        
    def __generadorProductos(self):
        for producto in self.__productos:
            yield producto
            
    def agregarProducto(self, producto):
        self.__productos.append(producto)
    
    def setProductos(self, productos):
        self.__productos = productos
        
    def totalOrden(self):
        total = 0
        for producto in self.__productos:
            total += producto.getPrecio()
        
        return total
        
    def __str__(self):
       datos = f"___ORDEN___\nID: {self.__id}\n"
       for producto in self.__productos:
           datos+= f"{producto}\n"
       return datos
    