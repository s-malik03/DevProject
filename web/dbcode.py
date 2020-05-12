import sqlite3

database = sqlite3.connect('example.db')
c = database.cursor()

c.execute('''CREATE TABLE information (CNIC text, PHONE text, ARRIVAL_TIME text, DEPARTURE_TIME text)''')

def insert(db):
    sql  = 'INSERT INTO information VALUES (%s, %s, %s, %s)'
    val  = (db.cnic, db.phone, db.arrival_time, db.departure_time)
    c.execute(sql, val)
    database.commit()
