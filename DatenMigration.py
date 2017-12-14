import csv
import re

with open('Data1.csv', newline='') as file:
    reader = csv.reader(file, delimiter=";")
    lineCounter = 1
    for entity in reader:
        entityValid = True
        entityCount = 0
        entityMessage = 'Concerned:'
        for entry in entity:
            if(entityCount == 0):
                if(not re.search('^\d+$',entry)):
                    entityValid = False
                    entityMessage+=",AddressNumber"
            elif(entityCount == 1):
                if(not re.search('[a-zA-Z\-\'\s]{5,}$',entry)):
                    entityValid = False
                    entityMessage += ",Surname/Lastname"
            elif (entityCount == 2):
                if(not re.search('^[a-zA-Zä-üÄ-Ü]{4,}\s{1}\d+[a-zA-Z]*$', entry)):
                    entityValid = False
                    entityMessage += "Street/Number"
            elif (entityCount == 3):
                if(not re.search('^[0-9]{4,5}\s{1}[a-zA-Zä-üÄ-Ü]{4,}$', entry)):
                    entityValid = False
                    entityMessage += ",Postalcode/City"
            elif (entityCount == 4):
                if(not re.search('^\d{3}(\s|\/)?\d{3}(\s|\/)?\d{2}(\s|\/)?\d{2}(\s|\/)?$', entry)):
                    entityValid = False
                    entityMessage += ",phonenumber"
            elif (entityCount == 5):
                if(not re.search('[a-zA-Z]+\.?[a-zA-Z]*\@{1}[a-zA-Z]+\.{1}[a-zA-Z]{2,3}', entry)):
                    entityValid = False
                    entityMessage += ",email"
            elif (entityCount == 6):
                if(not re.search('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', entry)):
                    entityValid = False
                    entityMessage += ",ipv4"
            elif (entityCount == 7):
                if(not re.search('^\d{1,2}(\.|\-|\\|\/){1}\d{1,2}(\.|\-|\\|\/){1}\d{4}$', entry)):
                    entityValid = False
                    entityMessage += ",date"
            entityCount+=1
        if(not entityValid):
            print('Failure ocurred in line: #' + str(lineCounter))
            print(entityMessage)
            print("\n")
        lineCounter+=1

