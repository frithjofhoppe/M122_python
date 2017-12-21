import re

class Validation(object):

    def addressNumber(self, entry):
        return re.search('^\d+$', entry)

    def name(self, entry):
        return re.search('^[a-zA-Z\-\'\s]{5,}$', entry)

    def street(self, entry):
       return re.search('^[a-zA-Zä-üÄ-Ü]{4,}\s{1}\d+[a-zA-Z]*$', entry)

    def postalCode(self, entry):
        return re.search('^[0-9]{4,5}\s{1}[a-zA-Zä-üÄ-Ü]{4,}$', entry)

    def phoneNumber(self, entry):
        return re.search('^\d{3}(\s|\/)?\d{3}(\s|\/)?\d{2}(\s|\/)?\d{2}(\s|\/)?$', entry)

    def email(self, entry):
        return re.search('^[a-zA-Z]+\.?[a-zA-Z]*\@{1}[a-zA-Z]+\.{1}[a-zA-Z]{2,3}$', entry)

    def ip(self, entry):
        return re.search('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', entry)

    def date(self, entry):
        return re.search('^\d{1,2}(\.|\-|\\|\/){1}\d{1,2}(\.|\-|\\|\/){1}\d{4}$', entry)