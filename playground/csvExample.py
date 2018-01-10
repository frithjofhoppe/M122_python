import csv as c

file = open('C:\\Users\Frithjof Hoppe\Desktop\Temporär\Python\\user.csv','r', newline='')
content = c.reader(file, delimiter=";")

for line in content:
    for tup in range(
            0, line.__len__()-1):
        if(tup == 0 and line.__getitem__(tup) == 'mail'):
            print(line)
