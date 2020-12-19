"""try:
    miArchivo = open("MiArchivo.txt", "w")
    miArchivo.write("Estoy agregando texto al arcihvo")
except Exception as ex:
    print("Error", ex)
    print(type(ex))
finally:
    miArchivo.close()

try:
    lectura = open("MiArchivo.txt", "r")
    print("Leyendo...")
    print(lectura.read())
except Exception as ex:
    print("Error", ex)
    print(type(ex))
finally:
    lectura.close()"""
    

lineas = ["Escribiendo líneas\n", "Por medio de\n", "Una lista\n", "En python\n"]
try:
    archivo = open("MiArchivo.txt", "w")
    archivo.writelines(lineas)
except Exception as ex:
    print("Error", ex)
    print(type(ex))
finally:
    archivo.close()
    
    
try:
    lectura = open("MiArchivo.txt", "r")
    print("Leyendo Modo normal...")
    print(lectura.read())    
    print()
    lectura.seek(0)
    print("Leyendo lineas (En forma de lista)...")    
    print(lectura.readlines())
    print()
    lectura.seek(0)
    print("Leyendo una linea...")
    print(lectura.readline())
    print(lectura.readline())
    print(lectura.readline())
except Exception as ex:
    print("Error", ex)
    print(type(ex))
else:
    print()
    print("Se ha leido el archivo correctamente")    
finally:
    lectura.close()
