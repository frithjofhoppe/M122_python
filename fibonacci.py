result = 0
def fibonacci(counter, a, b):
    localcounter = counter
    aa = a
    bb = b
    if(localcounter == 0):
        return aa
    else:
        localcounter -= 1
        aa, bb = bb, aa + bb
        fibonacci(localcounter, aa, bb)

print(fibonacci(25, 1, 0))

