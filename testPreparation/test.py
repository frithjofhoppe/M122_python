import testPreparation.validation as v

file = open('data', 'r',newline='\n')

counter = 1

lines = file.readlines()

for line in lines:
    strPrint = 'CARD ' + str(line) + ' '
    print("line:" + str(line) + "'")
    if(v.isValidMastercard(line)):
        strPrint += 'is valid Visacard'
    elif(v.isValidVisacard(line)):
        strPrint += 'is valid Mastercard'
    print(strPrint)
    counter+=1
