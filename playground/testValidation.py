import playground.validation as validate

print("Please enter following informations")

parameters = []

while True:
    strInput = input("Birtday:")
    if(not validate.birthday(strInput)):
        print("Incorrect format")
    else:
        parameters.append(str(strInput))
        break

print(parameters)

while True:
    strInput = input("PhoneNumber:")
    if(not validate.phoneNumber(strInput)):
        print("Incorrect format")
    else:
        parameters.append(strInput)
        break

print("Your informations")
for information in parameters:
    print(information)
