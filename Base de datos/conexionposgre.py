import psycopg2

#conexion = psycopg2.connect(host="localhost", database="testDb", user="postgres", password="12345")
conexion = psycopg2.connect(user='postgres', password="12345", host="localhost", database="testDb")

cursor = conexion.cursor()
sentencia = 'SELECT * FROM personas ORDER BY id' 
cursor.execute(sentencia)
datos = cursor.fetchall()

for dato in datos:
    print(dato)


cursor.close()
conexion.close()

