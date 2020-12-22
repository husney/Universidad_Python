import psycopg2

conexion = psycopg2.connect(user="postgres", password="12345", host="localhost", database="testDb")
cursor = conexion.cursor()

sql = "UPDATE personas SET nombre = %s, apellido = %s, email = %s WHERE id = %s"

valores = (("Update1", "update1", "update1",20), ("update2", "update2", "update2",21), ("update3", "update3", "update3", 22), ("update4", "update4", "update4",23))

cursor.executemany(sql, valores)
conexion.commit()

