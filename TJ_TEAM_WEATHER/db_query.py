import sqlite3

# query string to create visitor table
visitor_table = '''CREATE TABLE IF NOT EXISTS visitor(
                first_name TEXT, 
                last_name TEXT,
                enquiry_date datetime,
                vs_id INTEGER PRIMARY KEY AUTOINCREMENT) '''

# query string to create visit record table
visit_record_table = '''CREATE TABLE IF NOT EXISTS visit_record(
                info_request TEXT,
                date_request TEXT,
                currency REAL,
                info_id INTEGER,
                FOREIGN KEY(info_id) REFERENCES visitor(vs_id)) '''

# query string. Join table visitor and visit_record 
record_per_visit = '''SELECT  a.first_name +' '+a.last_name, b.info_request+' '+ b.date_request, b.currency
                FROM visitor AS a JOIN visit_record AS b
                ON a.vs_id = b.info_id
                WHERE a.vs_id = ?
                '''

#function create database, connection, and enforced the foreign key policy
def db_connection():
    conn = None #set connection to none
    try:
        conn = sqlite3.connect('visitor_db.sqlite') #create database connection
        #conn.execute('PRAGMA foreign_keys = ON') # enforce foreign key policy
        return conn 
    except: 
        return 'connection not established!'


weather_table = '''CREATE TABLE IF NOT EXISTS weather(
                fc_date TEXT, 
                fc_weather TEXT,
                fc_id INTEGER
                ) '''

'''
#query string. Join table Artwork_tbl and Artist_tbl to search all available artwork related to artist
available_artwork_query = SELECT a.rowid, a.artwork, a.price
                FROM artwork_tbl AS a JOIN artist_tbl AS b
                ON a.artist_id = b.artist_id
                WHERE b.artist_name = ? AND a.isSold = ?
                

'''