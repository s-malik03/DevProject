import datetime
from textwrap import dedent

class Arrival(object):
    def __init__(self, cnic, phone, time, token):
        self.cnic  = cnic
        self.phone = phone
        self.time  = time
        self.token = token
    def getter(self):
        return (dedent(f"""
            CNIC    : {self.cnic}
            Phone # : {self.phone}
            Time    : {self.time}
            Token   : {self.token}
                """))

while True:
    token = 0
    data_arrival = {}
    print("Arrival or Departure?")

    arrival_or_departure  = input(">")

    if "arrival" in arrival_or_departure:
        cnic  = input("")
        phone = input("")
        time  = datetime.datetime.now()
        token = token+1
        data_arrival[token] = Arrival(cnic, phone, time, token)
        ##print((data_arrival[token]).getter())

    print("End day?")
    if "yes" in input(">"):
        with open(f"{datetime.date.today()}.txt","w") as f:
            f.write(data_arrival[token].getter())

        break
