from flask import Flask, render_template, redirect, request, url_for, session,flash, request,jsonify
from flask_mysqldb import MySQL, MySQLdb
from sqlalchemy import text
import bcrypt

app = Flask(__name__)

app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_DB']='calculatedb'
app.config['MYSQL_CURSORCLASS']='DictCursor'
# Stop connect
mysql = MySQL(app)

@app.route("/")
def index():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM gpa')
    rows=cur.fetchall()
    
    return render_template("index.html",datas=rows) #นำ datas ไปแสดงผลที่หน้า html

@app.route("/calculate",methods=['POST','GET'])
def calculate():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM gpa')
    rows=cur.fetchall()
    # for row in rows :
    #     print(row)

    Subject = request.form.getlist("Subject[]") #รับค่าเป็นarray
    Unit = request.form.getlist("Unit[]")
    Grade = request.form.getlist("Grade[]")
    
    print("***********************************************************************")
    print(Subject,Unit,Grade)
    # Total1 = (float(Unit) * float(Grade))
    # print (Subject,Total1)
    print("***********************************************************************")
    
    return render_template("index.html",datas=rows)

if __name__== "__main__" :
    app.run(debug=True)