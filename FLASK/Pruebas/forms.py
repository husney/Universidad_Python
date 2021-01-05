from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from wtforms.fields.html5 import EmailField

#Validación personalizada
#form toma el formulario en uso
#field el campo que se está validando
def noHola(form, field):
    if field.data == "Hola":
        raise ValidationError("No se puede escribir hola en el campo")


class Persona(FlaskForm):
    nombre = StringField("nombre", validators=[
        DataRequired(message="El es campo requerido"),
        Length(max=50, min=2, message="El campo debe tener entre 2 a 50 caracteres"),
        noHola
        ],
    render_kw={"placeholder": "Nombre . . ."}
    )
    
    correo = EmailField("correo", validators=[
        DataRequired(message="El campo es requerido"),
        Email(),
        Length(max=50, min=10, message="El campo debe tener de 10 a 50 caracteres")
    ],
    render_kw={"placeholder": "Email . . ."}
    )
    
    telefono = StringField("telefono", validators=[
        DataRequired(message="El campo es requerido"),
        Length(max=15,min=7, message="El campo debe tener de 7 a 15 caracteres")
    ],
    render_kw={"placeholder": "Telefono . . ."}
    )
    
    submit = SubmitField("Enviar")