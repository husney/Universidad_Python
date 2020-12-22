import psycopg2

conexion = psycopg2.connect(user="postgres", password="12345", host="localhost", database="testDb")
cursor = conexion.cursor()

sql = "UPDATE personas SET nombre = %s, apellido = %s, email = %s WHERE id = %s"

valores = ("Laura", "Sanchez", "lausanchez@gmail.com", 17)
cursor.execute(sql, valores)
conexion.commit()

