#!/usr/bin/python3.5
# Skript M122

#Datei oeffnen und die Variable cpuinfo legen
cpuinfo = open('/proc/cpuinfo','r')

#Gibt Dateiverzeichnispfad zuruck
print(cpuinfo)
#Gibt den Dateiinhalt durch Iteration aus
for line in cpuinfo:
	print(line, end='')
#Gibt den Dateiinhalt ohne Iteration aus
print(cpuinfo.read())
#Gibt die erste Zeile aus
print(cpuinfo.readline())
#Gibt die zweite Zeile aus
print(cpuinfo.readline())
#Gibt den Inhalt als liste aus
print(cpuinfo.readlines())