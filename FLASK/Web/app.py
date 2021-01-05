from flask import Flask, render_template, url_for, request, session
from werkzeug.utils import redirect
from werkzeug.exceptions import abort

class User:

    def __init__(self, userName = None, password = None):
        self.__userName = userName
        self.__password = password

    def getUserName(self):
        return self.__userName

    def setUserName(self, userName):
        self.__userName = userName



app = Flask(__name__)
app.secret_key="MiLLaveSecreta"


#http://localhost:5000/
@app.route('/')
def index():
    if 'user' in session:
        return f"El usuario esta logueado {session['user']}"
    else:
        return "El usuario no se ha logueado"

@app.route("/Home")
def Home():
    return "Hola"

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['userName']
        return redirect(url_for('index'))
    else:
        return render_template('loging.html')

@app.route("/logout")
def logout():
     session.pop('user')
     return redirect(url_for('index'))

@app.route('/saludar/<nombre>')
def saludar(nombre):
    return f'Saludos {nombre.upper()}'

@app.route('/edad/<int:edad>')
def edadPage(edad):
    return f"Su edad es {edad}"

@app.route('/mostrar/<nombre>', methods=['POST','GET'])
def mostrarNombre(nombre):
    return render_template("Mostrar.html", Nombre = nombre)

@app.route("/redireccion")
def redireccion():
    return redirect(url_for('mostrarNombre',nombre="Husney"))


@app.route('/salir')
def salir():
    return abort(404)

@app.errorhandler(404)
def errorPaginaNoEncotrada(error):
    return render_template('Error404.html', error=error)


#REST Represantional State Transfer
#API Aplication Program Interface
@app.route('/api/mostrar/<string:nombre>', methods=["POST","GET"])
def mostrar_json(nombre):
    valores = {"nombre":nombre, "apellido":"Rincon", "lista":[1,2,3,4,5],"metodo_http":request.method}
    return valores