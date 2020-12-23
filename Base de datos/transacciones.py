import psycopg2

conexion = psycopg2.connect(user="postgres", password="12345", host="localhost", database="testDb")

try:
    cursor = conexion.cursor()
    sql1 = "INSERT INTO personas(nombre, apellido, email) VALUES (%s, %s ,%s)"
    valoresInsert = ("Laura", "Sanchez", "Lausanchez@gmail.com")
    cursor.execute(sql1, valoresInsert)
    
    sql2 = "UPDATE personas SET nombre = %s, apellido = %s, email = %s WHERE id = %s"
    valoresUpdate = ("Camila", "Calatraz", "camilacalatraz@gmail.com", 27)
    cursor.execute(sql2, valoresUpdate)
        
    conexion.commit()
except Exception as ex:
    print(f"Ha ocurrido un error en {ex}")
    conexion.rollback()
else:
    print("Se han guardado los datos correctamente")
finally:
    cursor.close()
    conexion.close()
    
