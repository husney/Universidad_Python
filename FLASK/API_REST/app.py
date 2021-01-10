from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = "12345"
api = Api(app)

class Productos(Resource):
    
    def get(self):



api.add_resource(Productos, '/productos')


if __name__ == "__main__":
    app.run(debug=True)