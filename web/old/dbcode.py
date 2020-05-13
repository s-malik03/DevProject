import sqlite3

database = sqlite3.connect('example.db')
c = database.cursor()
try:
    c.execute('''CREATE TABLE information (CNIC text, PHONE text, ARRIVAL_TIME text, DEPARTURE_TIME text)''')
except sqlite3.OperationalError:
    print("This ~~DATABASE~~ already exists")

def insert(db):
    sql  = "INSERT INTO information VALUES ({},{},{},{})".format('"'+db.cnic+'"', '"'+db.phone+'"', '"'+db.arrival_time+'"', '"'+db.departure_time+'"') #fixed string quotation mark issue
    c.execute(sql)
    database.commit() #added commit

def update(db):
    sql = "UPDATE information SET DEPARTURE_TIME = ({})".format('"'+db.departure_time+'"')
    c.execute(sql)
    database.commit()
