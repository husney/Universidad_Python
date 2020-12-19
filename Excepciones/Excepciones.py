

try: 
    10/0
except Exception as ex:
    print(f"Ha ocurrido un error \'{ex}\'")
finally:
    print("Se ha ejecutado la estrucutra try catch")
    print()
    

a = 10
b = 0
resultado = None

try:
    resultado = a / b
except ZeroDivisionError as ex:
    print(f"Error {ex}")
    print(type(ex))
except TypeError as ex:
    print(f"Error {ex}")
    print(type(ex))
except FileNotFoundError as ex:
    print(f"Error {ex}")    
    print(type(ex))
except Exception as ex:
    print(f"Error {ex}")
    print(type(ex))
    
print("El resultado es: ", resultado)   
    
print()
resultado = None
try:
    #a = input("Primer número: ")
    #b = input("Segundo número: ")
    retultado = a / b
except ZeroDivisionError as ex:
    print("Error", ex)
    print(type(ex))
except TypeError as ex:
    print("Error", ex)
    print(type(ex))
except Exception as ex:
    print("Error", ex)
    print(type(ex))
    
print()

try:
    print(10 / 2)
except Exception as ex:
    print("Error", ex)
    print(type(ex))
else:
    print("Se ha ejecutado sin problemas")
finally:
    print("Se termino la ejecución")
    

print("-------------------")

class MiExceptionNumerosIguales(Exception):
    
    def __init__(self, mensaje):
        self.message = mensaje


try:
    if 1 == 1:
        raise MiExceptionNumerosIguales("Error los números son iguales")
    else:
        print("Números diferentes")
except Exception as ex:
    print(ex)
    print(type(ex))
    