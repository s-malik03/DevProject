import datetime
from textwrap import dedent

class Arrival(object):
    def __init__(self, cnic, phone, time, token):
        self.cnic  = cnic
        self.phone = phone
        self.ar_time  = ar_time
        self.token = token
    def getter(self):
        return (dedent(f"""
            CNIC    : {self.cnic}
            Phone # : {self.phone}
            Arrival Time    : {self.ar_time}
            Token   : {self.token}
                """))
class Departure(object):
    def __init__(self, cnic, phone, time, token):
        self.cnic  = cnic
        self.phone = phone
        self.de_time  = de_time
        self.token = token
    def getter2(self):
        return (dedent(f"""
            CNIC    : {self.cnic}
            Phone # : {self.phone}
            departure Time    : {self.de_time}
            Token   : {self.token}
                """))

while True:
    token = 0
    data_arrival = {}
    data_departure = {}
    print("Arrival or Departure?")

    arrival_or_departure  = input(">")

    if "arrival" in arrival_or_departure:
        cnic  = input("Input CNIC ")
        phone = input("Input Phone Number")
        ar_time  = datetime.datetime.now()
        token = token+1
        print ("this is your token ", token )
        data_arrival[token] = Arrival(cnic, phone, ar_time, token)
        ##print((data_arrival[token]).getter())
    elif "departure" in arrival_or_departure:
        cnic  = input("Input CNIC ")
        phone = input("Input Phone Number")
        de_time  = datetime.datetime.now()
        token_input=int(input("input your token number"))
        data_departure[token_input] = Departure(cnic, phone, de_time, token)

    print("End day?")
    if "yes" in input(">"):
        with open(f"{datetime.date.today()}.txt","w") as f:
            f.write(data_arrival[token].getter())
            f.write(data_departure[token_input].getter2())

            f.close()



        break
#still in progress cuz were having difficulties dealing with the dictionaries
#at day end
