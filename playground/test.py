import os
from pathlib import Path

file = open('test','r')
path = 'C:\\Users\Frithjof Hoppe\Desktop\Temporär\Python\\user.csv'

if(os.path.exists(path)):
    os.remove(path)

csv = open(path,'w')

for line in file:
    arLine = line.split(':')
    strToAppend = ''
    for entry in range(0, arLine.__len__()-1):
        if(entry != arLine.__len__()-2):
            strToAppend += arLine.__getitem__(entry) + ";"
        else:
            strToAppend += arLine.__getitem__(entry)
        print(entry)
    csv.write('\n'+strToAppend)