from playground.classUser import User
import os
import platform

def getEntryByUser(strUser):
    source = open('test','r')
    for entry in source:
        splitted = entry.split(':')
        if(splitted.__getitem__(0) == strUser):
            return User(splitted.__getitem__(0),splitted.__getitem__(1))

def addUser(user):
    if(type(user) is User):
        source = open('test','a')
        source.write('\n'+user.getName()+':'+user.getNumber())