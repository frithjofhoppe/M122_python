def fibonacci2(wert):
    if(wert == 0):
        return 0
    elif(wert == 1):
        return 1
    else:
        return (fibonacci2(wert-1) + fibonacci2(wert-2))

counter = 0

while True:
    print (fibonacci2(counter))
    counter+=1
    if(counter == 25):
        break

