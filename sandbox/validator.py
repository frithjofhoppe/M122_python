import re

def isValidEmail(strIn):
    result = re.search('^[a-zA-Z]{1,}(\.[a-zA-Z]{1,})*\@[a-zA-Z]{1,}(\.[a-zA-Z]{1,})*\.[a-z]{2,3}$', strIn)
    if(result):
        return True;
    else:
        return False;
