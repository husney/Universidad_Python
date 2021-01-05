from flask import Flask, render_template,redirect, url_for, session
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/Saludo')
def saludo():
    return "Hola Mundo"


#Configuración de la Base de Datos

HOST = "localhost"
PORT = "5432"
USER = "postgres"
PASSWORD = "12345"
DATABASE = "SAP_FLASK"

FULL_URL_DB = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Configuración flask-migrate

migrate = Migrate()
migrate.init_app(app,db)

#clase de modelo ORM
#Para realizar un modelo debemos extender de la clase db.Model

#Crea la Tabla en la Base de Datos
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(25))
    apellido = db.Column(db.String(25))
    email = db.Column(db.String(50), unique=True)

    def __str__(self):
        return f'ID: {self.id}\nNombre: {self.nombre}\nApellido: {self.apellido}\nEmail: {self.email}'


@app.route('/')
@app.route('/index')
@app.route('/home')
def inicio():
    #Listar persona
    personas = Persona.query.all()
    totalPersonas = Persona.query.count()    
    app.logger.debug(f'Personas: {personas}')
    app.logger.debug(f'Número personas {totalPersonas}')
    return render_template('index.html', personas=personas, numeroPersonas = totalPersonas)

@app.route('/ver/<int:id>', methods=['GET'])
def verPersona(id):
    #persona = Persona.query.get(id) Puede lanzar un error en caso de que no exista
    #persona = Persona.query.get_or_404(id) #En caso de no encontrar el registro lanza el error 404 listo para el handler    
    persona = Persona.query.filter(Persona.id == id).first()
    app.logger.debug(f'Persona: {persona}')
    return render_template('persona.html', persona=persona)

@app.route('/agregar', methods=['GET'])
def agregarPersona():
    return render_template('agregar.html')