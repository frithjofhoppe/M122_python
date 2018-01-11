import re as regex

file = open('logo','r').read()
print(file)

def birthday(strIn):
    result = regex.search('^((3[0-1])|[0-2][0-9])(\.|\s)(0[1-9]|1[0-2])\\3(19[0-9][0-9])$', strIn)
    if(result):
        return True
    elif(not result):
        return False

def phoneNumber(strIn):
    result = regex.search('^(0[1-9]{2})(\-|\s|\\\)([0-9]{3})\\2([0-9]{4})$', strIn)
    if(result):
        return True
    else:
        return False