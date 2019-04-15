"""
Lösung zur Aufgabe 3 von Blatt 1
"""

def min(zahl1, zahl2, zahl3):
    if(zahl1 < zahl2 and zahl1 < zahl3):
        return zahl1
    elif(zahl2 < zahl3):
        return zahl2
    else:
        return zahl3

def max(zahl1, zahl2, zahl3):
    if(zahl1 > zahl2 and zahl1 > zahl3):
        return zahl1
    elif(zahl2 > zahl3):
        return zahl2
    else:
        return zahl3

print("Das Maximum von 2, -10, 25 ist: ", max(2, -10, 25))
print("Das Minimum von 2, -10, 25 ist: ", min(2, -10, 25))
