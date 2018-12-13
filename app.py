from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3



app = Flask(__name__)

app.secret_key = 'many random bytes'

class students(object):
    def __init__(self, idno, firstname, midname,lastname, gender, course, yearlevel):
        self.idno = idno
        self.fName = firstname
        self.mName = midname
        self.lName = lastname
        self.gender = gender
        self.course = course
        self.yrLevel = yearlevel

conn = sqlite3.connect('test.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS students(idno TEXT PRIMARY KEY, fname TEXT, mName TEXT,LName TEXT, gender TEXT, course TEXT,yrLevel TEXT )")
conn.commit()
conn.close()



@app.route('/')
def Index():
    connection = sqlite3.connect("test.db")
    crsr = connection.cursor()  
    crsr.execute("SELECT  * FROM students")
    data = crsr.fetchall()
    crsr.close()
    return render_template('index2.html', students=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        idno = request.form['idno']
        fName = request.form['firstname']
        mName = request.form['midname']
        lName = request.form['lastname']
        gender = request.form['gender']     
        course = request.form['course']
        yrlevel = request.form['yearlevel']
        with sqlite3.connect('test.db') as connection:

            crsr = connection.cursor()
            crsr.execute("INSERT INTO students (idno, fName, mName, lName, gender, course, yrlevel ) VALUES (?, ?, ?, ?, ?, ?, ?)", (idno, fName,mName,lName,gender,course,yrlevel))
            connection.commit()

        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    connection = sqlite3.connect('test.db')
    cur = connection.cursor()
    cur.execute("DELETE FROM students WHERE idNo=?", (id_data,))
    connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == "POST":
        id_data = request.form['idno']
        fName = request.form['firstname']
        mName = request.form['middlename']
        lName = request.form['lastname']
        gender = request.form['gender']     
        course = request.form['course']
        yrlevel = request.form['yearlevel']

        with sqlite3.connect('test.db') as connection:

            crsr = connection.cursor()
            crsr.execute("SELECT * FROM students")
            for row in crsr.fetchall():
                crsr.execute("UPDATE students SET fName=?, mName=?, lName=?, gender=?, course=?, yrLevel=? where idno =?",(fName, mName, lName, gender, course,yrlevel,id_data,))
                connection.commit()

    
    flash("Data Updated Successfully")
    return redirect(url_for('Index'))
    connection.close()









if __name__ == "__main__":
    app.run(debug=True)




