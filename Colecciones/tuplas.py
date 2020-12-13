frutas = ("Manzana", "Pera", "Uva")

print(frutas)
print(len(frutas))
print(frutas[0])
print(frutas[:3])

print(frutas[-1])
print(frutas[1:3])
listaFrutas = list(frutas)
listaFrutas.append("Durazno")
frutas = tuple(listaFrutas)
print(frutas)
del frutas

numeros = (13, 1, 8, 3, 2, 5, 8)
menores = []

for n in numeros:
    if n < 5:
        menores.append(n)

