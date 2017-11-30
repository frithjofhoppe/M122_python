cpuinfo = open('/proc/cpuinfo','r')
liste = cpuinfo.readlines()
print(liste[4] + liste[7])