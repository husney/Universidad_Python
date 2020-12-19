from Empleado import Empleado
from Gerente import Gerente


def detalles(padre):
    print(padre)
    print(type(padre))
    
e = Empleado("Sara", 3000000)
detalles(e)

print()

g = Gerente("Valentina Márin", 4000000, "Angeles")
detalles(g)

class Persona:
    
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def __str__(self):
        return f"Nombre: {self.__nombre}"

