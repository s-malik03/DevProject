#!C:/Users/User/AppData/Local/Programs/Python/Python38/python.exe
import db_lib
import datetime
import time
import cgi
import os
import cgitb
cgitb.enable()

date=datetime.datetime.now()

DB=db_lib.dbopen("{}-{}-{}.db".format(date.day,date.month,date.year))

Conn=DB.cursor()

var=os.environ["HTTP_COOKIE"]

cookie=var[4:]

x=""

try:

    db_lib.update(DB,Conn,cookie,time.ctime())

except Exception as e:

    x=e

Conn.close()

DB.close()

print("Content-type: text/html\r\n\r\n")

print("<html><body>GOODBYE!")

print(x)

print("</body></html>")
