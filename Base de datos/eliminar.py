import psycopg2


conexion = psycopg2.connect(user="postgres", password="12345", host="localhost", database="testDb")
cursor = conexion.cursor()


sql = "DELETE FROM personas WHERE id = %s"
valor = (25,)

cursor.execute(sql, valor)
conexion.commit()
 