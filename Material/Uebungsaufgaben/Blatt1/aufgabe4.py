"""
Lösung zur Aufgabe 4 vom Blatt 1
"""

def printPinCodes():
    for i in range(10000):
        ausgabe = str(i).zfill(4)
        print(ausgabe)

# Fals 0000 als Pin ausgeschlossen sein soll
def printPinCodes2():
    for i in range(9999):
        ausgabe = str(i+1).zfill(4)
        print(ausgabe)

printPinCodes()
