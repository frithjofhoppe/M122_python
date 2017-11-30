ram = open('/proc/meminfo','r')
ramlist = ram.readlines()

def getTotalRam():
    return ramlist[0]

def getFreeRam():
    return ramlist[1]

def getBuffers():
    return ramlist[3]

def getCache():
    return ramlist[4]