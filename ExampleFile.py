from DataFile import *

file = DataFile("testCsv.csv")
print(str(file.getRowCout()))
# file.appendEntry("g;Lukas;Bern")
print(str(file.getRowCout()))
file.removeEntryByColumnAndIdentifier(0,'g')