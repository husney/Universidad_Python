from flask import Flask, render_template, request, session, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from database import db
from models import Persona
from forms import PersonaForm


app = Flask(__name__)
app.secret_key="12345"

#app.config['SECRET_KEY'] = n


#Configuración DB
HOST = "localhost"
USER = 'postgres'
PASSWORD = '12345'
NAME_DB = "SAP"

FULL_URL_DB = f"postgresql://{USER}:{PASSWORD}@{HOST}/{NAME_DB}"

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)
#db = SQLAlchemy(app)
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

@app.route('/')
def index():
    personas = Persona.query.order_by('id').all()
    total = Persona.query.count()
    return render_template('index.html', personas=personas, total = total)

@app.route('/persona/<int:id>')
def verPersona(id):
    #Persona segun el id
    persona = Persona.query.get_or_404(id)
    return render_template('verPersona.html',  persona=persona)

@app.errorhandler(404)
def error404(error):
    return render_template('Error.html')



@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    persona = Persona()
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            db.session.add(persona)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('personaForm.html', formulario=personaForm)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    persona = Persona.query.get_or_404(id)
    personaForm = PersonaForm(obj=persona)
    if request.method == 'POST':
        if personaForm.validate_on_submit():
            personaForm.populate_obj(persona)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('editar.html', formulario=personaForm)

@app.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    return redirect(url_for('index'))

#if __name__ == '__main__':
#    app.run(debug=True)
