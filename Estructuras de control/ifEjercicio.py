
mes = int(input("Por favor ingrese un número que represente a un mes del año: "))

if mes == 1:
    print("Es Enero / January")
elif mes == 2:
    print("Es Febrero / February")
elif mes == 3:
    print("Es Marzo / March")
elif mes == 4: 
    print("Es Abril / April")
elif mes == 5:
    print("Es Mayo / May")
elif mes == 6:
    print("Es Junio / June")
elif mes == 7: 
    print("Es Julio / July")
elif mes == 8:
    print("Es Agosto / August")
elif mes == 9:
    print("Es Septiembre / September")
elif mes == 10:
    print("Es Octubre / October")
elif mes == 11:
    print("Es Noviembre / November")
elif mes == 12:
    print("Es Diciembre / December")
else:
    print("Error mes incorrecto") 
    
if mes in(12, 1, 2):
    print("Es invierno")
elif mes in(3, 4, 5):
    print("Es Pimavera")
elif mes in(6, 7, 8):
    print("Es Verano")
elif mes in(9, 10, 11):
    print("Es Otoño")
    
    
valor = int(input("Por favor ingrese un valor"))

if valor >8 and valor <11:
    print("A")
elif valor >7 and valor <10:
    print("B")
elif valor >6 and valor <8:
    print("C")
elif valor >5 and valor <7:
    print("D")
elif valor >= 0 and valor <6:
    print("F")
    
    