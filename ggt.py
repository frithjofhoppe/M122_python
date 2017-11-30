def ggt(a,b):
    aa = 0
    bb = 0
    rest = 10

    if(a > b):
        aa = a
        bb = b
    else:
        aa = b
        bb = a

    while rest != 0:
        rest = aa % bb
        yield aa / bb
        aa = bb
        bb = rest


result = ggt(90,8)

for x in result:
    print(str(x))