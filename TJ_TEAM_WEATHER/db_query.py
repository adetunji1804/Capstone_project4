import sqlite3
from datetime import datetime

# query string to create visitor table
visitor_table = """CREATE TABLE IF NOT EXISTS visitor(
                first_name TEXT, 
                last_name TEXT,
                enquiry_date datetime,
                vs_id INTEGER PRIMARY KEY AUTOINCREMENT) """

# query string to create visit record table
visit_record_table = """CREATE TABLE IF NOT EXISTS visit_record(
                info_request TEXT,
                date_request TEXT,
                currency REAL,
                info_id INTEGER,
                FOREIGN KEY(info_id) REFERENCES visitor(vs_id)) """

# query string. Join table visitor and visit_record
record_per_visit = """SELECT  a.first_name +' '+a.last_name, b.info_request+' '+ b.date_request, b.currency
                FROM visitor AS a JOIN visit_record AS b
                ON a.vs_id = b.info_id
                WHERE a.vs_id = ?
                """

weather_table = """CREATE TABLE IF NOT EXISTS weather(
                fc_date TEXT, 
                fc_weather TEXT,
                fc_id INTEGER
                ) """


obj_visitor = """INSERT INTO visitor (first_name, last_name, enquiry_date) 
                 VALUES (?, ?, ?) """


def db_connection(db_file):
    """create database, connection, and enforced the foreign key policy with db_flile parameter"""
    conn = None  # set connection to none
    try:
        conn = sqlite3.connect(db_file)  # create database connection
        conn.execute('PRAGMA foreign_keys = ON') # enforce foreign key policy
        return conn
    except:
        return "connection not established!"


def get_visitor_info(fname, lname):
    fname = input("Please provide your firstname: ")
    lname = input("And your lastname: ")
    date_now = get_current_date()
    return fname, lname, date_now


# return the date in prefered format
def get_current_date():
    current_date = datetime.today()
    return "{}/{}/{}".format(current_date.month, current_date.day, current_date.year)


def create_tables():
    with db_connection("visitor_db.sqlite") as conn:

        tables = [visitor_table, visit_record_table, weather_table]
        for table in tables:
            exec = conn.execute(table)
        return exec.rowcount
            


def create_visitor(obj_visitor):
    fname, lname, date_now = get_visitor_info("", "")
    with db_connection("visitor_db.sqlite") as conn:
        row_affected = conn.execute(obj_visitor, (fname, lname, date_now))
        if row_affected.rowcount > 0:
            return row_affected.lastrowid
            
    conn.close()



