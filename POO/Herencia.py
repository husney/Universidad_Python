class Persona:
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad
        
    
    def __str__(self):
        return f"{self.__nombre} {self.__edad}"

class Empleado(Persona):
    
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.__sueldo = sueldo
    
    def __str__(self):
        return super().__str__() + f" {self.__sueldo}"
        
        
p1 = Persona("Sara", 22)
print(p1) 
 
print()

emp1 = Empleado("Alejandra", 20, 1000000)
print(emp1)



class Vehiculo:
    
    def __init__(self, marca, ruedas):
        self.__marca = marca
        self.__ruedas = ruedas
    
    def __str__(self):
        return f"Marca: {self.__marca}\n Ruedas: {self.__ruedas}"

    def getMarca(self):
        return self.__marca
    
    def setMarca(self, marca):
        self.__marca = marca
    
    def getRuedas(self):
        return self.__ruedas
    
    def setRuedas(self, ruedas):
        self.__ruedas = ruedas
    
class Coche(Vehiculo):
    
    def __init__(self, marca, ruedas, placa):
        super().__init__(marca, ruedas)
        self.__placa = placa
        

class Bicicleta(Vehiculo):
    
    def __init__(self, marca, ruedas, cambios):
        super().__init__(marca, ruedas)
        self.__cambios = cambios
        
