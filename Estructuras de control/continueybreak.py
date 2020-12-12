
palabra = "Holanda"

for letra in palabra:
    if letra == "a":
        continue
    print(letra)

print("___________")

for letra in palabra:
    if letra == "a":
        break
    print(letra)
    

print("___________________")

for n in range(10):
    if n % 2 != 0:
        continue
    print(n )
    
    