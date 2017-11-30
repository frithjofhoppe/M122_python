import listecpuinfo
import listmemoryinfo as ram
import sys

cpu = listecpuinfo.getcpuinfo()

vendor = cpu[1]
model = cpu[4]
mhz = cpu[6]
cach = cpu[7]

# print(vendor+model+mhz+cach)
#
# print(ram.getFreeRam())
# print(ram.getTotalRam())
# print(ram.getBuffers())
# print(ram.getCache())
#
# print(dir())

toReturn = ""

print(sys.argv)
# Ersterr Eintrag aus der Liste beinhaltet den Namen der Datei
for eachArg in sys.argv:
    if(str(eachArg) == "vendor"):
        toReturn += vendor
    elif(eachArg == "model"):
        toReturn += model
    elif(eachArg == "mhz"):
        toReturn += mhz
    elif(eachArg == "cache"):
        toReturn += cach
    elif(eachArg == "freememory"):
        toReturn += ram.getFreeRam()
    elif(eachArg == "totalmemory"):
        toReturn += ram.getTotalRam()
    elif(eachArg == "buffers"):
        toReturn += ram.getBuffers()
    elif(eachArg == "cached"):
        toReturn += ram.getCache()
    else:
        print("./systeminfo.py <options>")
        print("Arguments:")
        print("venodr")
        print("model")
        print("mhz")
        print("cache")
        print("freememory")
        print("totalmemory")
        print("buffers")
        print("cached")

print(toReturn)