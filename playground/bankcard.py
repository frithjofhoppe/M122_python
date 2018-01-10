import re as regex

def isValidVisacard(strCard):
    result = regex.search('^\d{4}(\-|\s){1}\d{4}\\1\d{4}\\1\d{4}$', strCard)
    if(result):
        return True
    else:
        return False

def isValidMastercard(strCard):
    result = regex.search('^5[1-5]{1}\d{2}(\-|\s){1}\d{4}\\1\d{4}\\1\d{4}$', strCard)
    if(regex.match('^5[1-5]{1}\d{2}(\-|\s){1}\d{4}\\1\d{4}\\1\d{4}$', strCard)):
        return True
    else:
        return False

def isNumber(strNumber):
    if(regex.search('^\d*$', strNumber)):
        return True
    else:
        return False

def postalCode(entry):
    return regex.search('^[0-9]{4,5}\s{1}[a-zA-Zä-üÄ-Ü]{4,}$', entry)