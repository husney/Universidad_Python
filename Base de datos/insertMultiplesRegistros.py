import psycopg2

conexion = psycopg2.connect(user="postgres", password="12345", host="localhost", database="testDb")
cursor = conexion.cursor()


sql = "INSERT INTO personas(nombre, apellido, email) VALUES (%s, %s, %s)"

#datos = (("nombre1", "apellido1", "correo1"), ("nombre2", "apellido2", "correo2"), ("nombre3", #"apellido3", "correo3"), ("nombre4", "apellido4", "correo4"))

#for valores in datos:
    #cursor.execute(sql, valores)

datos = (("nombre5", "apellido5", "correo5"), ("nombre", "apellido", "correo"), ("nombre7", "apelido7", "correo7"), ("nombre8", "apellido8", "correo8"))

cursor.executemany(sql, datos)

conexion.commit()
registrados = cursor.rowcount
print(registrados)

     
     








