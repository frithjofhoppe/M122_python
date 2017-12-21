import csv
import os.path
from pathlib import Path

class DataFile(object):
    strPath = ""

    def __init__(self, path):
        self.strPath = path

    def getPath(self):
        return self.strPath

    def appendEntry(self, strEntry):
        with open(self.strPath, "a") as csvFile:
            if self.fileExists():
                c = csv.writer(csvFile, delimiter = ';')
                arEntry = strEntry.split(';')
                c.writerow(['a','b','c'])

    def removeEntryByColumnAndIdentifier(self, column, identifier):
        with open(self.strPath,'w+') as csvFile:
            if self.fileExists():
                c = csv.writer(csvFile, delimiter=';')
                originFile = []
                rowToRemove = 0
                for row in c:
                    originFile.append(row)
                    attributeCounter = 0
                    for attribute in row:
                        if(attributeCounter == column and attribute == identifier):
                            rowToRemove = attributeCounter
                originFile.pop(rowToRemove)
                print ('finished')

    def getRowCout(self):
        if(self.fileExists()):
            with open(self.strPath, newline='') as file:
                stream = csv.reader(file, delimiter=';')
                counter = 0
                for row in stream:
                    counter += 1
            return counter
        return 0

    def fileExists(self):
        f = Path(self.strPath)
        return f.is_file()