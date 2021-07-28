############# Script Details #################################################################

# Script Name            :  todo.py
# Script version         :  3.8.5
# Prepared By            :  naveen.kumar5@infinite.com
# Created_date           :  22-05-21
# last_modification_date :  22-05-21

##############################################################################################
# Purpose of the Script
#############################################################################################

# This script is designed such that many users sign in maintain their ToDo list
# The Ouput fetched data should be displayed on console

#############################################################################################
# Below points has been considered in the Script
#############################################################################################

# 1.Created a database in sqlite and created two tables one is for user record and another is for user details.

# 2.In the output console he must register and login

# 3.After login he must view his ToDO list

# 3.Designed script such a way that after the login sucessful he can maintain his ToDo list

# 4.A log file created with the current date time along with message specified.

##############################################################################################

# Imported logging  for log with the current date time along with message specified.
# Imported sqlite3 to work sqlite database
# Module flask was imported for to design api
# In flask imported render_template to work on html files
# In flask imported request to works various methods
import sqlite3
from flask import Flask, render_template, request
import logging

# The setting basic configuration of log_file format and level
logging.basicConfig(
    filename="todo.log",
    filemode="w",
    format="%(asctime)s :: %(message)s",
    level=logging.INFO,
)

# Flask construtor named of current module as arguments
app = Flask(__name__)

# This header  will store all header of ToDo list
header = ["TITLE", "DESCRIPTION", "CREATE_DATE", "DUE_DATE", "USER", "MARK"]

# Opening sqllite3 connecting to database and creating two static tables
with sqlite3.connect("user.db") as conn:
    logging.info("sucessfully connected to database")
    #Create table user for storing login credentials
    conn.execute('CREATE TABLE if not exists user (user TEXT primary key,password txt)')
    logging.info('user table is created')
    #Saving the changes in database
    conn.commit()
    logging.info("saving the changes")
    #Creating table details to store user ToDo list 
    conn.execute('CREATE TABLE if not exists details (title TEXT, description TEXT, create_date TEXT,due_date TEXT,user TEXT REFERENCES user(user),mark TEXT DEFAULT "no" )')
    logging.info('details table is created')
    #Saving the changes in database
    conn.commit()
    logging.info("saving the changes")

# URL binded with  '/' automatically calls login function works on only in post and get methods
# Return output in console
@app.route("/", methods=["POST", "GET"])
def login():
    # Here returning the login template
    logging.info("Successfully rendered login.html")
    return render_template("login.html")


# URL binded with  '/register' automatically calls register function works on only in post methods
# Return output in console
@app.route("/register", methods=["POST"])
def registartion():
    # Here returning the register template
    logging.info("Sucessfully rendered register.html ")
    return render_template("register.html")


# URL binded with  '/register_success' automatically calls register_sucess function works on only in post methods
# Return output in console
@app.route("/register_success", methods=["POST"])
def register_success():
    # Here we collecting some data as input using templates
    user = request.form.get("name")
    password = request.form.get("pwd")
    conform_password = request.form.get("cpwd")
    # Checking password is equal to conform_password or not
    if password == conform_password:
        logging.info("password is matched")
        # Opening sqllite3 connecting to database
        with sqlite3.connect("user.db") as conn:
            logging.info("sucessfully connected to database")
            # Establishing cursor in database
            cur = conn.cursor()
            # excuting query in database
            cur.execute("INSERT INTO user VALUES(?,?)", (user, password))
            conn.commit()
            logging.info("saving the changes")
        return "USER CREATED"
    else:
        logging.info("incorrect password")
        # Returning incorrect password
        return "INCORRECT PASSWORD"


# URL binded with  '/login' automatically calls log function works on only in post methods
# Return output in console
@app.route("/login", methods=["POST"])
def log():
    # Here we collecting some data as input using templates
    user = request.form.get("name")
    password = request.form.get("pwd")
    # Opening sqllite3 connecting to database
    with sqlite3.connect("user.db") as conn:
        logging.info("sucessfully connected to database")
        # Establishing cursor in database
        cur = conn.cursor()
        # excuting query in database
        user_check = cur.execute(
            f"SELECT * FROM user where user = ? ", (user,)
        ).fetchall()
        # Check fetching data is empty list or not
        if user_check == []:
            logging.info("it is empty list")
            return (
                f"THE USER:{user.upper()} DOESNOT EXIST PLEASE REGISTER AND TRY AGAIN "
            )
        # Checking password is equal to user password
        if user_check[0][1] == password:
            logging.info("user password is matches")
            # Opening sqllite3 connecting to database
            with sqlite3.connect("user.db") as conn:
                logging.info("sucessfully connected to database")
                # Establishing cursor in database
                cur = conn.cursor()
                # excuting query in database
                all = cur.execute(
                    f"select * from details where user = ? ", (user,)
                ).fetchall()
                logging.info(all)
                # Check fetching data is empty list or not
                if all == []:
                    logging.info("it is a empty list")
                    all = f"THERE IS NO DATA FOR USER:{user.upper()} "
                    # returning template login_sucess,html and return some variable to it
                    return render_template("login_sucess.html", name=all, user=user)
                else:
                    # Used a lst variable for store the fetched data
                    lst = []
                    # Looping the fetched data
                    for fetching_data in all:
                        # Used a dict variable for store ToDO list
                        dict = {}
                        # Initalising j=0
                        j = 0
                        # Looping the data to store key and value pair
                        for data in fetching_data:
                            # Accessing the dict1 and assigning column name as key
                            # Value as fetched data
                            dict[header[j]] = data
                            # j incrementing by 1
                            j += 1
                        logging.info(dict)
                        # Storing dict to lst for output
                        lst.append(dict)
                    logging.info(lst)
                    # Returning login_sucess.html with data and user name
                    return render_template("login_sucess.html", name=lst, user=user)
        else:
            logging.info("incorrect password")
             # Returning incorrect password
            return "INCORRECT PASSWORD"
        


# URL binded with  '/option' automatically calls option function works on only in post methods
# Return output in console
@app.route("/option", methods=["POST"])
def option():
    # Here we collecting some data as input using templates
    option = request.form.get("option")
    user = request.form.get("user")
    # Checking option equalto create
    if option == "create":
        logging.info("rendering to create.html")
        # Returning create.html and user name
        return render_template("create.html", user=user)
    # Checking option equalto delete
    if option == "delete":
        logging.info("rendering to delete.html")
        # Returning delete.html and user name
        return render_template("delete.html", user=user)
    # Checking option equalto update
    if option == "update":
        logging.info("rendering to update.html")
        # Returning update.html and user name
        return render_template("update.html", user=user)
    # Checking option equalto mark
    if option == "mark":
        logging.info("rendering to mark.html")
        # Returning mark.html and user name
        return render_template("mark.html", user=user)


# URL binded with  '/create' automatically calls create function works on only in post methods
# Return output in console
@app.route("/create", methods=["POST"])
def create():
    # Here we collecting some data as input using templates
    title = request.form.get("title")
    description = request.form.get("description")
    due_date = request.form.get("due_date")
    create_date = request.form.get("create_date")
    user = request.form.get("user")
    # Opening sqlite3 and connecting to db
    with sqlite3.connect("user.db") as conn:
        logging.info("sucessfully connected to database")
        query = "INSERT INTO DETAILS (title,description,create_date,due_date,user) VALUES (?,?,?,?,?)"
        values = (title, description, create_date, due_date, user)
        # Establishing cursor in database
        cur = conn.cursor()
        # Executing query in database
        cur.execute(query, values)
        logging.info("Data sucessfullly inserted")
        # Saving the changes
        conn.commit()
        logging.info("saved the changes in database")
        return "ITEM CREATED"


# URL binded with  '/delete' automatically calls delete function works on only in post methods
# Return output in console
@app.route("/delete", methods=["POST"])
def delete():
    # Here we collecting some data as input using templates
    title = request.form.get("title")
    user = request.form.get("user")
    # Opening sqlite3 and connecting to database
    with sqlite3.connect("user.db") as conn:
        logging.info("Sucessfully connected to database")
        all = conn.execute(
            f"select * from details where user = ? and title = ? ", (user, title)
        ).fetchall()
        logging.info("Sucessfully fetched data")
        # Checking the empty list or not
        if all == []:
            logging.info("It is a empty list")
            return f"THE USER:{user.upper()} HAD NO ITEM TITLE:{title}"
        # Checking title equal to title
        if all[0][0] == title:
            # Establishing cursor in database
            cur = conn.cursor()
            # Executing query in database
            cur.execute(
                f"DELETE FROM DETAILS WHERE TITLE = ? and user = ? ",
                (
                    title,
                    user,
                ),
            )
            logging.info("Excuted the query")
            # Saved the changes
            conn.commit()
            logging.info("Saved the changes in database")
            return "ITEM DELETED"
        else:
            # Return no such user
            return f"THE USER:{user.upper()} HAD NO SUCH ITEM TITLE:{title}"


# URL binded with  '/mark' automatically calls mark function works on only in post methods
# Return output in console
@app.route("/mark", methods=["POST"])
def mark():
    # Here we collecting some data as input using templates
    title = request.form.get("title")
    user = request.form.get("user")
    # Opening sqlite3 and connecting to database
    with sqlite3.connect("user.db") as conn:
        all = conn.execute(
            f"select * from details where user = ? and title = ? ", (user, title)
        ).fetchall()
        # Checking the empty list or not
        if all == []:
            logging.info("it is a empty list")
            return f"THE USER:{user.upper()} HAD NO ITEM TITLE:{title}"
        # Ehecking title equal to title
        if all[0][0] == title:
            # Checking mark equal to no
            if all[0][-1] == "no":
                query = f'UPDATE DETAILS SET MARK = "yes" WHERE TITLE = ? and user = ?'
                values = (
                    title,
                    user,
                )
                # Establishing cursor in database
                cur = conn.cursor()
                # Executing query
                cur.execute(query, values)
                logging.info("Executed query")
                # Saving the changes
                conn.commit()
                logging.info("saved the changes in database")
                return f"THE TITLE:{title} IS SETED HAS DONE "
            else:
                # Returning title is already exists in database
                return f"THE TITLE:{title} IS ALREADY DONE"
        else:
            # Return no such user
            return f"THE USER:{user.upper()} HAD NO SUCH ITEM TITLE:{title}"


# URL binded with  '/update' automatically calls update function works on only in post methods
# Return output in console
@app.route("/update", methods=["POST"])
def update():
    # Here we collecting some data as input using templates
    title = request.form.get("title")
    due_date = request.form.get("due_date")
    user = request.form.get("user")
    description = request.form.get("description")
    # Opening sqlite3 and connecting to database
    with sqlite3.connect("user.db") as conn:
        logging.info("sucessfully connected to database")
        all = conn.execute(
            f"select * from details where user = ? and title = ? ", (user, title)
        ).fetchall()
        # Checking the empty list or not
        if all == []:
            logging.info("it is a empty list")
            return f"THE USER:{user.upper()} HAD NO ITEM TITLE:{title}"
        # Checking title equal to title
        if all[0][0] == title:
            query = f"UPDATE DETAILS SET due_date = ?, description = ? WHERE TITLE = ? and user = ? "
            value = (
                due_date,
                description,
                title,
                user,
            )
            # Establishing cursor in database
            cur = conn.cursor()
            # Executing query
            cur.execute(query, value)
            logging.info("Executed query")
            # Saving the changes
            conn.commit()
            logging.info("saved the changes in database")
            return f"THE TITLE:{title} OF {user.upper()} ITEMS DATA IS UPDATED "
        else:
            # Return no such user
            return f"THE USER:{user.upper()} HAD NO ITEM TITLE:{title}"


# Checking main function or not
if __name__ == "__main__":
    # Setting Flask debug as true
    # And port = 5004
    app.run(debug=True, port=5004)
