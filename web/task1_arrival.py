#!C:/Users/User/AppData/Local/Programs/Python/Python38/python.exe
import datetime
import time
import db_lib
import cgi

def VerifyCNIC(CNIC):

    try:

        int(CNIC)

    except:

        print("INVALID CNIC")

        exit()

    if len(CNIC)!=13:

        print("INVALID CNIC")

        exit()

class Arrival(object):
    def __init__(self, cookie, cnic, phone, arrival_time, departure_time):
        self.cookie=cookie
        self.cnic  = cnic
        self.phone = phone
        self.arrival_time  = arrival_time
        self.departure_time = departure_time

    def change_departure_time(self, new):
        self.departure_time = new

def main():

    date=datetime.datetime.now()

    DB=db_lib.dbopen("{}-{}-{}.db".format(date.day,date.month,date.year))

    Conn=DB.cursor()

    db_lib.create_table(Conn)

    cookie=str(int(time.time()))

    print("Set-Cookie:UID = {}; Max-Age=10000000;".format(cookie))

    print("Content-type: text/html\r\n\r\n")
    
    data=cgi.FieldStorage()

    cnic=data["cnic"].value

    VerifyCNIC(cnic)

    number=data["number"].value

    try:

        if number[0]=="+":

            int(number)

        else:

            int(number)
    
    except:

        print("INVALID NUMBER")

        exit()

    arrival_time=time.ctime()

    data_arrival=Arrival(cookie,cnic,number,arrival_time,'0')

    db_lib.insert(DB, Conn, data_arrival)

    Conn.close()

    DB.close()

    print('<html><body><meta http-equiv="refresh" content=0;url="/thankyoupage.html"/></body></html>')

main()
