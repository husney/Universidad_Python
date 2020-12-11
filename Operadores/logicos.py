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
    