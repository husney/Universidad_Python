from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, Length
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import EmailField

class PersonaForm(FlaskForm):

    nombre = StringField('nombre', validators=[
        DataRequired(message='El campo es requerido'),
        Length(min=2, max=25, message='El campo debe tener entre 2 a 25 carácteres')
    ],
    render_kw={'placeholder':'Nombre . . .'}
    )

    apellido = StringField('apellido', validators=[
        DataRequired(message='El campo es requerido'),
        Length(min=2, max=25, message='El campo debe tener entre 2 a 25 carácteres')
    ],
    render_kw={'placeholder':'Apellido . . .'}
    )

    email = EmailField('email', validators=[
        Email(),
        DataRequired(message='El campo es requerido'),
        Length(min=13, max=50, message='El campo debe tener entre 13 a 50 carácteres')
    ],
    render_kw={'placeholder':'Email . . .'}
    )

    submit = SubmitField('Guardar')