import playground.bankcard as card
import re as regex

print(bool(card.isValidMastercard('5354 5655 5000 5556')))
print(bool(card.isValidMastercard('5354-5655-5000-5556')))
print(bool(card.isValidVisacard('4523 5689 9874 5556')))
print(bool(card.isValidVisacard('4523-5689-9874-5556')))

if(regex.search('(?<=5)[a-zA-Z]*','5asdfsdf')):
    print("TRUE")
else:
    print("FALSE")