from app import db

class Persona(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(25), nullable=False)
    apellido = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f"Id:{self.id}\nNombre: {self.nombre}\nApellido: {self.apellido}\nEmail: {self.email}"