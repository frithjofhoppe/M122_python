
def fibonacci():
    numA = 1
    numB = 1
    while True:
        yield numA
        temp = numA
        numA += numB
        numB = temp

liste = fibonacci()
counter = 0

for x in liste:
    print(str(x))
    if(counter == 20):
        break
    counter+=1