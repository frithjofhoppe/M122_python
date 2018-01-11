
def factorial(intCount):
    if(intCount == 0):
        return 1
    else:
        return factorial(intCount-1)*intCount

for x in range(0,15):
    print(str(factorial(x)))