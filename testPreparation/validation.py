import re as regex

def name(strIn):
    strIn = strIn.replace(chr(10),'')
    result = regex.search('^\w+\s\w+([\'\-]?\w+[\'\-]?)+\w+$', strIn)
    if(result):
        return True
    else:
        return False

def isValidVisacard(strCard):
    strCard = strCard.replace(chr(10), '')
    result = regex.search('^\d{4}(\-|\s){1}\d{4}\\1\d{4}\\1\d{4}$', strCard)
    if(result):
        return True
    else:
        return False

def isValidMastercard(strCard):
    strCard = strCard.replace(chr(10), '')
    result = regex.search('^5[1-5]{1}\d{2}(\-|\s){1}\d{4}\\1\d{4}\\1\d{4}$', strCard)
    if(result):
        return True
    else:
        return False