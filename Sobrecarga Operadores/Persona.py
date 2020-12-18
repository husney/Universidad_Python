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
        
    def __add__(self, b):
       self.__nombre += b.__nombre
       return self.__nombre
        
p1 = Persona("Sara" ,22)
p2 = Persona("Alejandra ", 20)

print(p1 + p2)


print(p1.getNombre())    

# + __add__(self, otro)
# - __sub__(self, otro)
# * __mul__(self, otro)
# / __truediv(self, otro)
# //__floordiv(self, otro)
# %__mod__(self, otro)
# **__pow__(self, otro)

# < __lt__(self, otro)
# > __gt__(self, otro)
# <= __le__(self, otro)
# >= __ge__(self, otro)

# += __iadd__(self, otro)
# -= __isub__(self, otro)
# *= __imul__(self, otro)
# /= __idiv__(self, otro)
# // __ifloordiv__(self, otro)
# % __imod__(self, otro)
# ** __ipow__(self, otro)
