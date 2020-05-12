from flask_wtf import FlaskForm
from wtforms import Form, IntegerField, StringField, DateField, DateTimeField, SubmitField
from wtforms.validators import Required


class AppointmentForm(FlaskForm):

    firstName = StringField("firstName", validators=[Required("Debes ingresar un nombre")])
    lastName = StringField("lasttName", validators=[Required("Debes ingresar un apellido")])
    ident = StringField("ident", validators=[Required("Debes ingresar una identificacion")])
    date = DateField("date", validators=[Required("Debes ingresar una fecha de naciemiento")])
    city = StringField("city", validators=[Required("Debes ingresar la ciudad")])
    neighborhood = StringField("neighborhood", validators=[Required("Debes ingresar el barrio")])
    mobile = StringField("mobile", validators=[Required("Debes ingresar un celular")])
    dateAppointment = DateTimeField("dateAppointment", validators=[Required("Debes ingresar la fecha de la cita")])

    submit = SubmitField('Submit')

