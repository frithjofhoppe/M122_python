from DataFile import *

file = DataFile("testCsv.csv")
print(str(file.getRowCout()))
file.appendEntry("Andrea;Lukas;Bern")
print(str(file.getRowCout()))