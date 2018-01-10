import re

string1 = 'hjhj787hj7hjh8hj'

objBack = re.search('[\d]+', string1)

print(objBack.group(0))