import psycopg2

conexion = psycopg2.connect(user="postgres", password="12345", host="localhost", database="testDb", port="5432")

cursor = conexion.cursor()


sql = "INSERT INTO personas (nombre, apellido, email) VALUES (%s, %s, %s)"
valores = ("Sara", "Garcia", "SGarcia@gmail.com")
cursor.execute(sql, valores)
conexion.commit() #Hace commit en la DB
insertados = cursor.rowcount
print(f"Registros insertados:  {insertados}")

