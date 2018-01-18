import testPreparation.validation as v

file = open('data', 'r',newline='\r\n')

counter = 1

lines = file.readlines()

for line in lines:
    strPrint = 'CARD ' + str(line) + ' '

    temp = line
    "".join(temp)
    print("line:" + str(line) + "'")
    if(v.isValidVisacard(temp)):
        strPrint += 'is valid Visacard'
    elif(v.isValidMastercard(temp)):
        strPrint += 'is valid Mastercard'
    print(strPrint)
    counter+=1
