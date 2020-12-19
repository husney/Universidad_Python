from Empleado import Empleado
class Gerente(Empleado):

    def __init__(self, nombre, sueldo, departamento):
        Empleado.__init__(self, nombre, sueldo)
        self.__departamento = departamento

    def getDepartamento(self):
        return self.__departamento

    def setDepartamento(self, departamento):
        self.__departamento = departamento

    def __str__(self):
        return Empleado.__str__(self) + f"\nDepartamento: {self.__departamento}"