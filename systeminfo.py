import listecpuinfo
import listmemoryinfo as ram
import sys

cpu = listecpuinfo.getcpuinfo()

vendor = cpu[1]
model = cpu[4]
mhz = cpu[7]
cach = cpu[8]

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
for arg in sys.argv:

    value = str(arg)

    if(value == "vendor"):
        toReturn += str(vendor)
    elif(value == "model"):
        toReturn += str(model)
    elif(value == "mhz"):
        toReturn += str(mhz)
    elif(value == "cache"):
        toReturn += str(cach)
    elif(value == "freememory"):
        toReturn += ram.getFreeRam()
    elif(value == "totalmemory"):
        toReturn += ram.getTotalRam()
    elif(value == "buffers"):
        toReturn += ram.getBuffers()
    elif(value == "cached"):
        toReturn += ram.getCache()
    # else:
    #     print("./systeminfo.py <options>")
    #     print("Arguments:")
    #     print("venodr")
    #     print("model")
    #     print("mhz")
    #     print("cache")
    #     print("freememory")
    #     print("totalmemory")
    #     print("buffers")
    #     print("cached")

print(toReturn)