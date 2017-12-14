import csv

with open('Data1.csv', newline='') as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        print('New line')
        for col in row:
            print(str(col))