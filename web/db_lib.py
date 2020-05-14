import sqlite3
import traceback

def dbopen(dbname):
    c=sqlite3.connect(str(dbname))
    return c

def create_table(cursor):
    try:
        cursor.execute('''CREATE TABLE information (Cookie text, CNIC text, PHONE text, ARRIVAL_TIME text, DEPARTURE_TIME text)''')

    except sqlite3.OperationalError:

        return 1

def insert(database,cursor,data):
    sql  = "INSERT INTO information VALUES ({},{},{},{},{})".format('"'+data.cookie+'"', '"'+data.cnic+'"', '"'+data.phone+'"', '"'+data.arrival_time+'"', '"'+data.departure_time+'"') #fixed string quotation mark issue
    
    try:

        cursor.execute(sql)

    except Exception as e:

        print(e)


    database.commit() #added commit

def update(database,cursor,key,data):
    sql = "UPDATE information SET DEPARTURE_TIME = ({}) WHERE Cookie = {}".format('"'+data+'"','"'+key+'"')
    
    cursor.execute(sql)

    database.commit()


def read(cursor):

    cursor.execute("SELECT * FROM information")

    data=cursor.fetchall()

    return data

