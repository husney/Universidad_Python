class MiClase:
    
    var_clase = 0
    
    
    var_staic = "Hola"
    
    def __init__(self, nombre):
        self.__nombre = nombre
        MiClase.var_clase += 1
        
    @staticmethod
    def saludar():
        print("Hola")
        
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre = nombre
        
print(MiClase.var_clase)

obj1 = MiClase("Prueba")

print(MiClase.var_clase)

obj2 = MiClase("Prueba2")

print(MiClase.var_clase)


MiClase.saludar()