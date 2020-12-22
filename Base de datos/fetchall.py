import psycopg2

conexion = psycopg2.connect(user="postgres", password="12345", host="localhost", port="5432", database="testDb")

cursor = conexion.cursor()
sql = "SELECT * FROM personas WHERE id IN %s"
valores = ((1,2,9),)
cursor.execute(sql, valores)
datos = cursor.fetchall()

for persona in datos:
    print(persona)

cursor.close()
conexion.close()