import csv
import playground.validation as val

strPath = 'C:\\Users\Frithjof Hoppe\Desktop\Temporär\Python\csv1.CSV'

file = open(strPath, 'r')
read = csv.reader(file, delimiter=';')
for line in read:
    print("\nLine")
    print(val.phoneNumber(line[1]))
    print(val.birthday(line[2]))

# writer = csv.writer(file, delimiter=';', quotechar='\'')

# writer.writerow(['5','023 465 7894','mx@test.ch'])