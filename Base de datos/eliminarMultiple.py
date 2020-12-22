import psycopg2

conexion = psycopg2.connect(user="postgres", password="12345", host="localhost", database="testDb")
cursor = conexion.cursor()

sql = "DELETE FROM personas WHERE id IN %s"
valores = ((24,26,27),)
cursor.executemany(sql, valores)



