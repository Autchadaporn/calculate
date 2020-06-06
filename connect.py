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
 
    Subject = request.form.getlist("Subject[]") #รับค่าเป็น list จากform index.html
    Unit = request.form.getlist("Unit[]")
    Grade = request.form.getlist("Grade[]")

    # ---------------------- start  ส่งค่าแล้วprintออกมาเป็นjson -------------------------
    # headers = ('Subject', 'Unit', 'Grade')
    # values = (
    #     request.form.getlist('Subject[]'),  
    #     request.form.getlist('Unit[]'),  
    #     request.form.getlist('Grade[]'),         
    # )
    # items = [{} for i in range(len(values[0]))]
    # for x,i in enumerate(values):  #enumerate เป็นคำสั่งสำหรับแจกแจงค่า index และข้อมูลใน index ในรูปแบบทูเพิล (Tuple) ดังนี้ (Index,Value) โดยต้องใช้กับข้อมูลชนิด list
    #     for _x,_i in enumerate(i): 
    #         items[_x][headers[x]] = _i
    # return jsonify(items)
    # -------------------- stop  ส่งค่าแล้วprintออกมาเป็นjson-----------------------

    print("***********************************************************************")
    print('วิชา:',Subject)
    print('หน่วยกิต:',Unit)
    print('เกรด:',Grade)
    print("***********************************************************************")
   
    #------------------------- start หาค่าผลรวมของหน่วยกิต ---------------------------
    sum =0
    for x in range(len(Unit)):
        #print(float(Unit[x])) #หน่วยกิตแต่ละตัว อ้างจาก x คือ index
        sum = sum + (float(Unit[x]))
    print('ผลรวมหน่วยกิต =',sum)
    #--------------------------- Stop หาค่าผลรวมของหน่วยกิต -------------------------
    
    print("***********************************************************************")
    total =0 
    for x in range(len(Unit)):
        for i in range(len(Grade)):
            if i == x: #ถ้า index ของ Unit และ Grade เท่ากัน ให้นำมาคำนวณ
                sum1 = (float(Unit[x])* float(Grade[i])) # หน่วยกิต คูณ เกรด
                # print(sum1)
                total = total+sum1 # หน่วยกิต คูณ เกรด มา บวกกัน เช่น (3*4.0)+(3*3.5)
    print('ผลรวม หน่วยกิต*เกรด =',total)
    print("***********************************************************************")
    GPA = total / sum
    GPA = '%.2f'%(GPA) # ตัดทศนิยมให้เหลือ 2 ตำแหน่ง เช่น 2.9642857142857144 เป็น 2.96
    print(GPA)
    
    return render_template("index.html",datas=rows,item=GPA)

if __name__== "__main__" :
    app.run(debug=True)