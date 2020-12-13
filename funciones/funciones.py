
def decoador(funcion):
    def decora(*args, **kwargs):
        print("Decornado")
        return print(funcion(*args, **kwargs))
    return decora

@decoador
def sumar(n1, n2):
    return n1 + n2

def saludar():
    print("Hola")
    


sumar(4, 2) 