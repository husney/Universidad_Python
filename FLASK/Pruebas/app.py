from flask import Flask, redirect, render_template, url_for, request
from forms import Persona
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = "12345"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'servicios'
mysql = MySQL(app)


@app.route('/')
@app.route('/inicio')
@app.route('/home')
def index():    
    return render_template('home.html')

@app.route('/nosotros')
def nosotros():
    return "Página de Nosotros"

@app.route('/servicios')
def servicios():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM serviciosDetalle')
    datos = cursor.fetchall()
    servicios = []
    for dato in datos:
        servicio = Servicio(dato[0],dato[1],dato[2],dato[3],dato[4])
        servicios.append(servicio)
    return render_template('servicios.html', servicios=servicios)

@app.route('/servicio/<id>')
def servicio(id):
    cursor = mysql.connection.cursor()
    cursor.execute(f'SELECT * FROM serviciosDetalle WHERE id = {id}')
    datos = cursor.fetchone()
    if datos == None:
        return render_template('servicioNoExiste.html')
    servicio = Servicio(datos[0], datos[1], datos[2], datos[3], datos[4])
    return render_template('servicio.html', servicio=servicio)

@app.route('/contacto')
def contacto():
    return "Página de contacto"

@app.route('/servicios/detalle/<service>')
def servicioDetalle(service):
    return f"El servicio <strong>{service}</strong>"

@app.route('/servicios/detalle/dos/<s1>/<s2>')
def servicios_dos(s1, s2):
    return f"Los servicios son : {s1}  | {s2}"

@app.route('/formularioS', methods=['GET','POST'])
def formularioS():
    if request.method =='POST':
        return f"Nombre: {request.form['nombre']} Email: {request.form['email']} Telefono {request.form['telefono']}"    
    else:
        return render_template('formularioS.html')
    
@app.route('/formularioObjeto', methods=['GET', 'POST'])
def formularioObjeto():
    formulario = Persona()
    if formulario.validate_on_submit():
        return f"Nombre: {request.form['nombre']} Email: {request.form['email']} Telefono {request.form['telefono']}"    
    return render_template('formularioObjeto.html', form=formulario)
    
class Servicio():
    
    def __init__(self,id, titulo, slug, detalle, foto):
        self.id = id
        self.titulo = titulo
        self.slug = slug
        self.detalle = detalle
        self.foto = foto

if __name__ == "__main__":
    app.run(debug=True)
