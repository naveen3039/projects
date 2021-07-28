############# Script Details #################################################################

# Script Name            :  with_api_connect_db.py
# Script version         :  3.8.5
# Prepared By            :  naveen.kumar5@infinite.com
# Created_date           :  21-05-21
# last_modification_date :  21-05-21

##############################################################################################
# Purpose of the Script
#############################################################################################

# This script is designed to connect local database and fetch data based on condition
# The Ouput fetched data should be displayed on console or text file

#############################################################################################
# Below points has been considered in the Script
#############################################################################################

# 1.Created a database in sqlite and created a table by using this script

# 2.After creating table inserting data to table by using  this script

# 3.With or Without condition Data was fetched through console

# 4.A log file created with the current date time along with message specified.

##############################################################################################

# Imported logging  for log with the current date time along with message specified.
# Imported sqlite3 to work sqlite database
# Module flask was imported for to design api
# In flask imported jsonify to display output in json format

from flask import Flask, jsonify
import sqlite3
import logging

# The setting basic configuration of log_file format and level
logging.basicConfig(
    filename="api.log",
    filemode="w",
    format="%(asctime)s :: %(message)s",
    level=logging.INFO,
)

# Flask construtor named of current module as arguments
app = Flask(__name__)

# This is static data used to insert in the table
books = [
    {
        "id": 0,
        "title": "A Fire Upon the Deep",
        "author": "Vernor Vinge",
        "first_sentence": "The coldsleep itself was dreamless.",
        "year_published": "1992",
    },
    {
        "id": 1,
        "title": "The Ones Who Walk Away From Omelas",
        "author": "Ursula K. Le Guin",
        "first_sentence": "With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.",
        "year_published": "1973",
    },
]

# This header will store all keys to use in specific required
header = list(books[0].keys())

# URL binded with  '/' automatically calls home function
# Return output in console
@app.route("/")
def home():
    # Connecting sqlite database to api
    conn = sqlite3.connect("database.db")
    # Checking connection was established or not
    if conn:
        connection = "DB IS CONNECTED"
        logging.info("Database is connected")
    else:
        connection = "DB IS NOT CONNECTED"
        logging.info("Database is not connected")
    return connection


# URL binded with  '/<id>' automatically calls id function
# In <id> we need to specify the id
# Return output in console
@app.route("/<id>")
def id(id):
    # Connecting sqlite database to api
    conn = sqlite3.connect("database.db")
    logging.info("Database is connected")
    # Establishing Cursor in sqlite3
    cur = conn.cursor()
    logging.info("Cursor estabished in database")
    # Executing Query in sqlite3 and fetching data
    all = cur.execute(f"SELECT * FROM books where id = {id} ;").fetchall()
    logging.info(f"Fetched id={id} data in table")
    # Used a lst variable for store the fetched data
    lst = []
    # Looping the fetched data
    for fetch_data in all:
        # Used a dict1 variable for store column name as key
        # Value as fetched data
        dict1 = {}
        # Initalising j=0
        j = 0
        # Looping the data to store key and value pair
        for data in fetch_data:
            # Accessing the dict1 and assigning column name as key
            # Value as fetched data
            dict1[header[j]] = data
            # j incrementing by 1
            j += 1
        # Storing dict1 to lst for output
        lst.append(dict1)
    # Checking the fetched data equal to [] or not
    if all == []:
        logging.info(f"id:{id} was not present ")
        lst = f"id:{id} is not present "
    # Returning data in json data
    return jsonify(lst)


# URL binded with  '/all' automatically calls all function
# Return output in console
@app.route("/all")
def all():
    # Connecting sqlite database to api
    conn = sqlite3.connect("database.db")
    logging.info("Database is connected")
    # Establishing Cursor in sqlite3
    cur = conn.cursor()
    logging.info("Cursor estabished in database")
    # Executing Query in sqlite3 and fetching data
    all = cur.execute("SELECT * FROM books;").fetchall()
    print(all)
    logging.info(f"Fetched all data in table")
    # Used a lst variable for store the fetched data
    lst = []
    # Looping the fetched data
    for fetch_data in all:
        # Used a dict1 variable for store column name as key
        # Value as fetched data
        dict1 = {}
        # Initalising j=0
        j = 0
        # Looping the data to store key and value pair
        for data in fetch_data:
            # Accessing the dict1 and assigning column name as key
            # Value as fetched data
            dict1[header[j]] = data
            # j incrementing by 1
            j += 1
        # Storing dict1 to lst for output
        lst.append(dict1)
    # Return the json data
    return jsonify(lst)


# URL binded with  '/create' automatically calls create function
# Return output in console
@app.route("/create")
def create():
    # Opening sqlite3 and connecting to database
    with sqlite3.connect("database.db") as conn:
        logging.info("Database is connected")
        query = f"CREATE TABLE books (id NUMERIC PRIMARY KEY,title TEXT,author TEXT,first_sentence TEXT,year_published TEXT)"
        # Query executing in database
        conn.execute(query)
        logging.info("Table  is created")
        # Saved the change made in database
        conn.commit()
        logging.info("Saved the Changes in Database")
    return "table created"


# URL binded with  '/insert' automatically calls insert function
# Return output in console
@app.route("/insert")
def insert():
    # Opening sqlite3 and connecting to database
    with sqlite3.connect("database.db") as conn:
        logging.info("Database is connected")
        # Establishing Cursor in sqlite3
        cur = conn.cursor()
        logging.info("Cursor estabished in database")
        # Looping Static Data
        for data in books:
            query = f"INSERT INTO books VALUES(?,?,?,?,?)"
            values = tuple(data.values())
            # Executing Query in database
            conn.execute(query, values)
            logging.info("Data inserted in Database")
            # Saving the changes in database
            conn.commit()
            logging.info("Saved the Changes in database")
    return "data inserted"


# Checking main function or not
if __name__ == "__main__":
    # Setting Flask debug as true
    # And port = 5004
    app.run(debug=True, port=5004)
