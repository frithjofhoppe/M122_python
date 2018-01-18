from pathlib import Path
import csv
import sandbox.validator as v

source = Path("C:\\Users\Frithjof Hoppe\Desktop\Temporär\Python\\Data1.csv");
file = open(source, 'r')
reader = csv.reader(file, delimiter=';')

positive = [];
negative = [];

for line in reader:
    if(v.isValidEmail(line[5])):
        positive.append("++ " + line[5]);
    else:
        negative.append("-- " + line[5]);

for entry in positive:
    print(entry);

for entry in negative:
    print(entry);