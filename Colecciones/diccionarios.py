# llave key (Array asociativo)
# "key": value

dicconario = { 
    "IDE": "Integrated Development Enviroment",
    "OOP": "Object Oriented Programing",
    "DBMS": "Database Management System"
}

print(dicconario.keys())
print(dicconario.values())
print(dicconario.get("OOP"))

dicconario["IDE"] = "INTEGRATED DEVELOPMENT ENVIROMENT"
print(dicconario["IDE"])

for llave in dicconario:
    print(dicconario[llave])
print("---------------")
for valor in dicconario.values():
    print(valor)
    
print("------------")

print("IDE" in dicconario)


dicconario["PK"] = "Primary Key"
print(dicconario["PK"])

del dicconario["PK"]
print(dicconario)

dicconario.pop("IDE")
print(dicconario)


dicconario.clear()

del dicconario

    