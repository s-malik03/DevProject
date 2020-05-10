#IN PROGRESS
import time
import datetime

class Individual:

    def __init__(self, CNIC, Phone, ArrivalTime, DepartureTime):

        self.CNIC=CNIC
        self.Phone=Phone
        self.ArrivalTime=ArrivalTime
        self.DepartureTime=DepartureTime

def VerifyCNIC(CNIC):

    try:

        int(CNIC)

    except:

        print("INVALID CNIC")

        return 1

    if len(CNIC)!=13:

        print("INVALID CNIC")

        return 1

def main():

    while True:

        fname=str(input("Enter name of file to search:"))

        try:

            f=open(fname,'r')

            break

        except:
                
            print("ERROR OPENING FILE!")


    CNICQuery=input("Enter CNIC to initiate query (do not put '-'):")

    while VerifyCNIC(CNICQuery)==1:

        CNICQuery=input("Enter CNIC to initiate query (do not put '-'):")

    Person=[]

    for l in f:

        ls=l.split('~')

        Person.append(Individual(ls[0],ls[1],ls[2],ls[3].rstrip('\n')))

    for ID in Person:

        if ID.CNIC==CNICQuery:

            print("FOR INDIVIDUAL IN QUESTION:\n#\nCNIC: {}\nNUMBER: {}\nARRIVALTIME: {}\nDEPARTURETIME: {}\n#".format(ID.CNIC,ID.Phone,ID.ArrivalTime,ID.DepartureTime))

            AT=ID.ArrivalTime

            DT=ID.DepartureTime

            break

    ArrivalTime=datetime.datetime.strptime(str(AT),"%a %b %d %H:%M:%S %Y")

    DepartureTime=datetime.datetime.strptime(str(DT),"%a %b %d %H:%M:%S %Y")

    for ID in Person:

        AT=datetime.datetime.strptime(str(ID.ArrivalTime),"%a %b %d %H:%M:%S %Y")

        DT=datetime.datetime.strptime(str(ID.DepartureTime),"%a %b %d %H:%M:%S %Y")

        if ID.CNIC!=CNICQuery:

            if ((float(AT.timestamp())>=float(ArrivalTime.timestamp())) and (float(AT.timestamp())<float(DepartureTime.timestamp()))) or ((float(DT.timestamp())>float(ArrivalTime.timestamp())) and (float(DT.timestamp())<float(DepartureTime.timestamp()))):

                print("\n#MATCH#\nCNIC: {}\nNUMBER: {}\nARRIVALTIME: {}\nDEPARTURETIME: {}\n#".format(ID.CNIC,ID.Phone,ID.ArrivalTime,ID.DepartureTime))

    f.close()

main()



    
        
