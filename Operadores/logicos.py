a = int(input("Ingrese un valor: "))

min = 0
max = 5

dentroRango = a >= min and a <= max
print(dentroRango)

if dentroRango:
    print("Dentro del rango")
else:
    print("Fuera de rango")
    
    
descanso = False
vacaciones = True

if descanso or vacaciones:
    print("Puedo ir a donde quiera")
else:
    print("Tengo deberes")
    
if not (descanso or vacaciones):
    print("Tengo deberes")
else:
    print("Puedo ir a donde quiera")


alto = int(input("Por favor ingrese el alto"))
ancho = int(input("Por favor ingrese el ancho"))

area = alto * ancho
perimetro = (alto + ancho) * 2

print(f"Area: {area}")
print(f"Perimetro: {perimetro}")


numero1 = int(input("Por favor ingrese el primer número"))
numero2 = int(input("Por favor ingrese el segundo número"))

if numero1 > numero2:
    print(f"El número mayor es {numero1}")
else:
    print(f"El número mayor es {numero2}")
