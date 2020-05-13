import db_lib
import datetime
import time
import cgi
import os

date=datetime.datetime.now()

DB=db_lib.dbopen("{}-{}-{}.db".format(date.day,date.month,date.year))

Conn=DB.cursor()

var=os.environ["HTTP_COOKIE"]

cookie=var[4:]

db_lib.update(DB,Conn,cookie,time.ctime())

Conn.close()

DB.close()

print("Content-type: text/html\r\n\r\n")

print("<html><body>GOODBYE!")

print("</body></html>")
