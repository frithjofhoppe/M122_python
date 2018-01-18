from pathlib import Path
import os
import csv

file = Path("C:\\Users\Frithjof Hoppe\Desktop\Temporär\Python\\result.csv")
writemod = "a"

if(file.exists()):
    answer = input("Breits extistierende Datei überschreiben? (y\\n)");
    if(answer == "y"):
        os.remove(file)

wr = open(file,writemod, newline='')
writer = csv.writer(wr, delimiter=';')

while True:
    firstname = input("Vorname:");
    lastname = input("Nachname: ");
    birthday = input("Geburtsdataum: ");
    print("\n");
    question = input("Noch ein Eintrag (y\\n)");
    writer.writerow([firstname,lastname,birthday]);
    if(question != "y"):
        break;

writer.close();