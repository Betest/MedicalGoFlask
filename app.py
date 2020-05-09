from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="appointmentapp"
)

app = Flask(__name__)


# Rutas
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

        return redirect(url_for('home'))




# Ejecutar la app en el server / en modo debug

if __name__ == "__main__":
    app.run(debug=True)