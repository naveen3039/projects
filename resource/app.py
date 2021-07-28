import sqlite3
from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash

with sqlite3.connect('database.db') as conn:
    conn.execute('CREATE TABLE if not exists user (user TEXT primary key,password txt)')
    conn.commit()
    conn.execute("CREATE TABLE if not exists details (user TEXT PRIMARY KEY ,SNo INTEGER SERIAL, Emp_ID INT,\
                  Name TEXT,Job_grade TEXT,IBM _Laptop_Status TEXT,Position_in_IBM TEXT,Designation_in_Infinite TEXT, \
                  status TEXT,Date_Of_Joining_Infinite char(50),Last_working_Date char(50),PO_no INT,PO_start_date char(50), \
                  PO_end_date char(50),IBM_Manager TEXT,Account_Manager TEXT,IBM_Emp_ID INT,IBM_Mail_ID char(50),\
                  Emp_Location TEXT,Experience INT,Per_day_rate_$ char(50),Per_day_rate_INR char(50),CTC char(50),\
                  CTC_in_$ char(50),GM char(50),Actual_billing_date char(50),Mobile_Number INT(10),Under_taking_letter char(50),\
                  Skill_set char(100),Laptop_received_date char(50),Address char(50))")
    conn.commit()

app = Flask(__name__)    

@app.route('/',methods=["POST","GET"])
def home():
    print(request.url_root)
    return render_template('login.html')

@app.route('/reg',methods=["POST"])
def reg():
    return render_template('register.html')

@app.route('/register',methods=["POST","GET"])
def register():
    if request.method == 'POST':
        user=request.form.get('user')
        password = request.form.get('password')
        conform_password=request.form.get('cpassword')
        if password == conform_password :
            with sqlite3.connect('database.db') as conn:
                usernames=conn.execute('select  * from user').fetchall()
                for names in usernames:
                    if user == names[0]:
                        return 'username already exists'
                pass1=generate_password_hash(password)
                conn.execute('INSERT INTO user VALUES(?,?)',(user,pass1))
                return f'{user} was registered sucessfully'
        else:
            return 'incorrect password'

@app.route('/login',methods=["POST"])
def login():
    user=request.form.get("user")
    password = request.form.get("password") 
    count = 0
    with sqlite3.connect('database.db') as conn:
        usernames=conn.execute('select  * from user').fetchall()
        for names in usernames:
            if user == names[0]:
                if password == str(names[1]):
                    return ''
                else:
                    return 'incorrect password'
            else:
                count = 0
        if count == 0:
            return 'admin not exists please register in  register portal'








if __name__ == '__main__':
    app.run(debug=True,port=5004)