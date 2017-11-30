def getcpuinfo():
    cupinfo = open('/proc/cpuinfo','r')
    liste = cupinfo.readlines()
    return liste