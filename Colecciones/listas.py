nombres = ["Santi", "Sara", "Alejandra"]
print(len(nombres))
print(nombres)
print(type(nombres))
nombres.append("Valentina Marin")
print(nombres)
nombres.insert(0, "Camila")
print(nombres)
del nombres[1]
print(nombres)
nombres.remove("Camila")
print(nombres)
nombres.pop(2)
print(nombres)
nombres.insert(0, "Valentina marin")
print(nombres)
nombres.pop()
print(nombres)
print(nombres[0])
nombres.append("Alejandra")
nombres.insert(0, "Sara Orrego")
print(nombres)
print(nombres[-1])
print(nombres[0:])
print(nombres)
print(nombres[0:2])
print(nombres[0:3])
print(nombres[:3])
print(nombres[1:])
nombres[3] = "Alejandra duque"
print(nombres)

print("________________")

for nombre in nombres:
    print(nombre)
    
if "Valentina marin" in nombres:
    print("Si existe")
else:
    print("No existe")


