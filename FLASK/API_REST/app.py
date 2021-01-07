from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = "12345"
api = Api(app)

class Productos(Resource):
    def __init__(self):
        self.productos = {
            "1":"Camisa",
            "2":"Zapatos",
            "3":"Pantaloneta",
            "4":"Medias",
            "5":"Bolsos"
        }

    def get(self):
        return self.productos

    def post(self, id, producto):
        return {"estado": "Guardando datos"}

    def put(self, id, producto):
        return {"estado":"Actualizando datos"}

    def delete(self, id):
        return {"estado":"Eliminando"}


api.add_resource(Productos, '/productos', '/productos/<id>/<producto>', '/productos/<id>')
#api.add_resource(Productos, )


if __name__ == "__main__":
    app.run(debug=True)