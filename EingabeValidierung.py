import re

print('Folgende Angaben eingeben')
txtvorname = input('Vorname:')
txtnachname = input('Nachname:')
txtstrasse = input('Strasse')
txthausnummer = input('Hausnummer:')
txtplz = input('PLZ:')
txtort = input('Ort:')
txtemail = input('Email:')
txtgeburtsdatum = input('Geburtsdatum:')
txtpostkonotnummer = input('Konto:')

while (True):
    if(not re.search('^[a-zA-Z]{2,}$',txtvorname)):
        print('Vorname => Gross- Kleinbuchstabe , mindestens 2 Zeichen')
        txtvorname = input('Vorname:')
    else:
        break

while (True):
    if(not re.search('^[a-zA-Z]{2,}$',txtnachname)):
        print('Nachname => Gross- Kleinbuchstabe , mindestens 2 Zeichen')
        txtnachname = input('Nachname:')
    else:
        break

while (True):
    if(not re.search('^[a-zA-Z]{5,}$',txtstrasse)):
        print('Strasse => Gross- Kleinbuchstabe , mindestens 5 Zeichen')
        txtstrasse = input('Strasse:')
    else:
        break

while (True):
    if(not re.search('^[0-9]{1,4}',txthausnummer)):
        print('Hausnummer => Zahlen , mindestens 1, maximal 4 Zeichen')
        txthausnummer = input('Hausnummer:')
    else:
        break

while (True):
    if(not re.search('[0-9]{4,5}',txtplz)):
        print('PLZ => Zahlen , mindestens 1, maximal 4 Zeichen')
        txtplz = input('PLZ:')
    else:
        break

while (True):
    if(not re.search('[a-zA-Z]{2,}',txtort)):
        print('Ort => Gross- Kleinbuchstaben , mindestens 2 Zeichen')
        txtort = input('Ort:')
    else:
        break

while (True):
    if(not re.search('[a-zA-Z]+\.?[a-zA-Z]*\@{1}[a-zA-Z]+\.{1}[a-zA-Z]{2,3}', txtemail)):
        print('Mail => max.mustermann@email.com')
        txtemail = input('Mail:')
    else:
        break

while (True):
    if(not re.search('[0-9]{1,2}(\.|\-){1}[0-9]{1,2}(\.|\-){1}[0-9]{4}',txtgeburtsdatum)):
        print('Geburtsdatum => 01-11-2017 | 1-1-2017')
        txtgeburtsdatum = input('Geburtsdatum:')
    else:
        break

while (True):
    print('Geburtsdatum => 01-11-2017 | 1-1-2017')
    if(not re.search('[0-9]{2}(\s|\-){1}[0-9]{6}(\s|\-){1}[0-9]{1}',txtpostkonotnummer)):
        print('Postkonto => 11-123456-7')
        txtpostkonotnummer = input('Postkonto:')
    else:
        break

print('Zusammenfassung')
print('vorname: ' + txtvorname)
print('nachname: ' + txtnachname)
print('strasse: ' + txtstrasse)
print('hausnummer: ' + txthausnummer)
print('plz: ' + txtplz)
print('ort: ' + txtort)
print('txtpostkonotnummer: ' + txtpostkonotnummer)





