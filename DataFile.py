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
        with open(self.strPath, 'a', newline='') as csvFile:
            if self.fileExists():
                c = csv.writer(csvFile, delimiter = ';')
                arEntry = strEntry.split(';')
                c.writerow([arEntry[0],arEntry[1],arEntry[1]])

    def removeEntryByColumnAndIdentifier(self, column, identifier):
        originFile = []
        with open(self.strPath,'r') as csvFile:
            if self.fileExists():
                c = csv.reader(csvFile, delimiter = ';')
                rowToRemove = 0
                for row in c:
                    originFile.append(row)
                    attributeCounter = 0
                    for attribute in row:
                        if(attributeCounter == column and attribute == identifier):
                            rowToRemove = attributeCounter
                originFile.pop(rowToRemove)
                print ('finished')
        with open(self.strPath, 'w') as csvFile:
            writer = csvFile.write(originFile)

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