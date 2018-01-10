def ggt(a, b):
    numA = a
    numB = b

    if(a > b):
        temp = numA
        numA = numB
        numB = temp

    while numA % numB != 0:
        temp = numB
        numB, numA = numA % numB, temp
    return numB

print(str(ggt(24,36)))


