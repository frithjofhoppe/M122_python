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
        if self.fileExists():
            c = csv.writer(open(self.strPath))
            arEntry = str.split(';', strEntry)
            c.writerRow([arEntry[0], arEntry[1], arEntry[2]])


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