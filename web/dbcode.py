import sqlite3

db = sqlite3.connect('example.db')
c = db.cursor()

c.execute('''CREATE TABLE information (CNIC, PHONE, ARRIVAL_TIME, DEPARTURE_TIME)''')

def insert(db):
    sql  = "INSERT INTO information VALUES (%s, %s, %s, %s)"
    val  = (db.cnic, db.phone, db.arrival_time, db.departure_time)
    c.execute(sql, val)
