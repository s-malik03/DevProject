import datetime

class Arrival(object):
    def __init__(self, cnic, phone, time, token):
        self.cnic  = cnic
        self.phone = phone
        self.time  = time
        self.token = token



while True:

    token = 0
    data_arrival = []
    print("Arrival or Departure?")

    arrival_or_departure  = input(">")

    if "arrival" in arrival_or_departure:
        assert len(cnic) == 14
        cnic  = input("")
        phone = input("")
        time  = datetime.datetime.now()
        token = token+1
        token = Arrival(cnic, phone, time, token)
#not done yet
