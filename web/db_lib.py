import sqlite3

def dbopen(dbname):
    c=sqlite3.connect(str(dbname))
    return c

def create_table(cursor):
    try:
        cursor.execute('''CREATE TABLE information (CNIC text, PHONE text, ARRIVAL_TIME text, DEPARTURE_TIME text)''')
    except sqlite3.OperationalError:
        print("This ~~DATABASE~~ already exists")

def insert(database,cursor,data):
    sql  = "INSERT INTO information VALUES ({},{},{},{})".format('"'+data.cnic+'"', '"'+data.phone+'"', '"'+data.arrival_time+'"', '"'+data.departure_time+'"') #fixed string quotation mark issue
    cursor.execute(sql)
    database.commit() #added commit

def update(database,cursor,key,data):
    sql = "UPDATE information SET DEPARTURE_TIME = ({}) WHERE CNIC = {}".format('"'+db.departure_time+'"')
    cursor.execute(sql)
    database.commit()


def read(cursor):

    cursor.execute("SELECT * FROM information")

    data=cursor.fetchall()

    return data

