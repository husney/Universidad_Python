from Producto import Producto
from Orden import Orden

zapatos = Producto("Zapatos", 90000)
camisa = Producto("Camisa", 40000)
pantalon = Producto("Pantalon", 70000)

 
productos = [zapatos, camisa, pantalon]

orden = Orden(productos)
print(orden)

print(orden.totalOrden())

reloj = Producto("Reloj", 80000)
orden.agregarProducto(reloj)

print(orden.totalOrden())





 