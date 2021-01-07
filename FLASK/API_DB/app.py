from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "TIENDA"

mysql = MySQL(app)
api = Api(app)

class Productos(Resource):

    def get(self):
        cursor = mysql.connect.cursor()
        cursor.execute('SELECT id, nombre, descripcion, precio, fecha FROM Productos')
        datos = cursor.fetchall()
        content = []
        for dato in datos:
            content.append({'id': dato[0],'nombre':dato[1],'descripcion':dato[2],'precio':dato[3], 'fecha':dato[4]})
        return jsonify(content)

    def post(self):
        try:
            cursor = mysql.connect.cursor()
            cursor.execute('INSERT INTO Productos(nombre, descripcion, precio) VALUES (%s, %s, %s)',(
                request.json['nombre'],
                request.json['descripcion'],
                request.json['precio']
            ))
            cursor.connection.commit()
            return jsonify({"Estado":"Producto guardado correctamente"})
        except Exception as ex:
            return jsonify({"Estado":"Error al registrar producto"})

    def put(self):
        try:
            cursor = mysql.connect.cursor()
            cursor.execute(
                'UPDATE Productos SET nombre = %s, descripcion = %s, precio = %s, fecha = now() WHERE id = %s', (
                    request.json['nombre'],
                    request.json['descripcion'],
                    request.json['precio'],
                    request.json['id']
                ))
            cursor.connection.commit()
            return jsonify({"estado":"Registro actualizado correctamente"})
        except Exception as ex:
            return jsonify({"estado":f"Error{ex}"})

    def delete(self):
        try:
            cursor = mysql.connect.cursor()
            cursor.execute("DELETE FROM Productos WHERE id = %s",(request.json['id']))
            cursor.connection.commit()
            return jsonify({"estado":"Registro eliminado correctamente"})
        except Exception as ex:
            return jsonify({"estado":f"Error {ex}"})


class ProductoId(Resource):

    def get(self, id):
        cursor = mysql.connect.cursor()
        cursor.execute(f'SELECT id, nombre, descripcion, precio, fecha FROM Productos WHERE id = {id}')
        datos = cursor.fetchone()
        content = {'id':datos[0],'nombre':datos[1], 'descripcion':datos[2], 'precio':datos[3], 'fecha':datos[4]}
        return jsonify(content)



api.add_resource(Productos, '/productos')
api.add_resource(ProductoId, '/productos/<id>')

if __name__ == ("__main__"):
    app.run(debug=True)