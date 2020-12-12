nombreLibro = input("Por favor ingrese el nombre del libro: ")
nombrePersona = input("Por favor ingrese el nombre de la persona que adquiere el libro: ")
precio = float(input("Por favor ingrese el precio del libro: "))
envioGratuito = int(input("¿El envio es gratuito?\n1=Si\n2=No: "))

if envioGratuito == 1:
    envioGratuito = True
elif envioGratuito == 2:
    envioGratuito = False
else:
    envioGratuito = None
    
    
print("Libro: " + nombreLibro)
print("Compro: " + nombrePersona)
if(envioGratuito):
    print("Envio gratuito")
    print("Precio:",precio)
else:
    print("Precio:",precio + 9000)
