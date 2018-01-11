#!/bin/python3.5
# Skript: M122_Scripts/python/fib_rek.py

print("Fibonacci-Generator mit Rekursion")

def fibonacci(zahl):
    if(zahl == 0):
        return 0
    elif(zahl == 1):
        return 1
    else:
        return fibonacci(zahl-1) + fibonacci(zahl-2)

counter = 0
while True:
    print("fib(" + str(counter) + ") = " + str(fibonacci(counter)))
    counter += 1
    if (counter > 25): break