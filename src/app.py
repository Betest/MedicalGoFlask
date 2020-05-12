from flask import Flask, render_template, request, redirect, url_for, flash
from form import AppointmentForm

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="appointmentapp"
)

app = Flask(__name__)

#settings
app.secret_key = 'secretkey'

#form = AppointmentForm(request.form)



# Rutas
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/home')
def root():
    return render_template('home.html')

@app.route('/')
def home():
    sql = "SELECT * FROM appointments"
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    res = mycursor.fetchall()

    return render_template('home.html', appointments = res)

@app.route('/createappointment')
def createappointment():
    return render_template('create-appointment.html')

# Mamejo de peticiones Add Appointment


@app.route('/addappointment', methods=['POST'])
def addappointment():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        ident = request.form['ident']
        date = request.form['date']
        city = request.form['city']
        neighborhood = request.form['neighborhood']
        mobile = request.form['mobile']
        dateAppointment = request.form['dateAppointment']

        mycursor = mydb.cursor()
        sql = f"INSERT INTO appointments (firstName, lastName, ident, date, city, neighborhood, mobile, dateAppointment) VALUES('{firstName}','{lastName}','{ident}','{date}','{city}','{neighborhood}','{mobile}','{dateAppointment}')"
        mycursor.execute(sql)        
        mydb.commit()

        flash('Cita agregada correctamente!')

        return redirect(url_for('home'))

@app.route('/editappointment/<id>')
def editappointment(id):
    mycursor = mydb.cursor()    
    mycursor.execute(f'SELECT * FROM appointments WHERE id = {id}')
    data = mycursor.fetchall()
    print(data)
    return render_template('edit-appointment.html', appointment = data[0])

@app.route('/updateappointment/<id>', methods=['POST'])
def updateappointment(id):
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        ident = request.form['ident']
        date = request.form['date']
        city = request.form['city']
        neighborhood = request.form['neighborhood']
        mobile = request.form['mobile']
        dateAppointment = request.form['dateAppointment']
        mycursor = mydb.cursor()
        mycursor.execute("""UPDATE appointments SET firstName = %s, lastName = %s, ident = %s, date = %s, city = %s, neighborhood = %s, mobile = %s, dateAppointment = %s WHERE id = %s""", (firstName, lastName, ident, date, city, neighborhood, mobile, dateAppointment, id))
        flash('Cita actualizada correctamente!')
    return redirect(url_for('home'))


@app.route('/deleteappointment/<int:id>')
def deleteppointment(id):
    sql = "DELETE FROM appointments WHERE id = {0}".format(id)
    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()

    flash('Cita eliminada correctamente!')

    return redirect (url_for('home'))



    
# Ejecutar la app en el server / en modo debug

if __name__ == "__main__":
    app.run(host="localhost", port=5000 ,debug=True)