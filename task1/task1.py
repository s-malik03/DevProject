import datetime
from textwrap import dedent

class Arrival(object):
    def __init__(self, cnic, phone, time, token, departure_time):
        self.cnic  = cnic
        self.phone = phone
        self.time  = time
        self.token = token
        self.departure_time = departure_time
    def getter(self):
        return (dedent(f"""
            CNIC      : {self.cnic}
            Phone #   : {self.phone}
            Time      : {self.time}
            Token     : {self.token}
            Departure : {self.departure_time}
                """))
    def change_departure_time(self, new):
        self.departure_time = new

#change the format as mentioned in task1.txt
token = 0
data_arrival   = {}
while True:


    print("Arrival or Departure?")

    arrival_or_departure  = input(">")
    a = True
    if "arrival" in arrival_or_departure:
        cnic = input("Input CNIC Number")
        phone = input("Input Phone Number")
        time  = datetime.datetime.now()
        data_arrival[token] = Arrival(cnic, phone, time, token, '0')
        print(data_arrival)
        print(token)
        token += 1

        ##print((data_arrival[token]).getter())
    elif "departure" in arrival_or_departure:
        user_token = int(input("Input token>"))
        Arrival.change_departure_time((data_arrival[user_token]) , datetime.datetime.now() )

    print("End day?")
    if "yes" in input(">"):
        f = open(f"{datetime.date.today()}.txt","w")
        for i in range(token):
            f.write(data_arrival[i].getter())
            
        f.close()
        break
