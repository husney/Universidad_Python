#No tienen orden y los elementos son  unicos
#No se pueden modificar pero si agregar y eliminar


planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)
print(len(planetas))
print("Marte" in planetas)
planetas.add("Tierra")
print(planetas)
planetas.discard("Jupiter") #No lanza error al eliminar un valor que no encuentre
print(planetas)