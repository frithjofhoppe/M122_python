class User:
    name = ''
    num = ''

    def __init__(self, name, num):
        self.num = num
        self.name = name

    def getName(self):
        return self.name

    def getNumber(self):
        return self.num