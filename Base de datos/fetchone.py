import psycopg2

conexion = psycopg2.connect(user="postgres", password="12345", host="localhost", database="testDb")
cursor = conexion.cursor()

sql = "SELECT * FROM personas WHERE id = %s"
idPersona = input("Inserte el id de la persona a buscar: ")
valores = (idPersona,)
cursor.execute(sql, valores)
datos = cursor.fetchone()
print(datos)

cursor.close()
conexion.close()
