import csv
import re
from Validation import Validation

val = Validation()

with open('Data1.csv', newline='') as file:
    reader = csv.reader(file, delimiter=";")
    lineCounter = 1
    for entity in reader:
        entityValid = True
        entityCount = 0
        entityMessage = 'Concerned:'
        for entry in entity:
            if(entityCount == 0):
                result = val.addressNumber(entry)
                if(not val.addressNumber(entry)):
                    entityValid = False
                    entityMessage+=",AddressNumber"
            elif(entityCount == 1):
                if (not val.name(entry)):
                    entityValid = False
                    entityMessage += ",Surname/Lastname"
            elif (entityCount == 2):
                if (not val.street(entry)):
                    entityValid = False
                    entityMessage += "Street/Number"
            elif (entityCount == 3):
                if (not val.postalCode(entry)):
                    entityValid = False
                    entityMessage += ",Postalcode/City"
            elif (entityCount == 4):
                if (not val.phoneNumber(entry)):
                    entityValid = False
                    entityMessage += ",phonenumber"
            elif (entityCount == 5):
                if (not val.email(entry)):
                    entityValid = False
                    entityMessage += ",email"
            elif (entityCount == 6):
                if (not val.ip(entry)):
                    entityValid = False
                    entityMessage += ",ipv4"
            elif (entityCount == 7):
                if (not val.date(entry)):
                    entityValid = False
                    entityMessage += ",date"
            entityCount+=1
        if(not entityValid):
            print('Failure ocurred in line: #' + str(lineCounter))
            print(entityMessage)
            print("\n")
        lineCounter+=1

