"""
Lösung zur Aufgabe 5 vom Blatt 1
"""

def summeDerQuadrate(ende):
    ergebnis = 0
    for zahl in range(ende):
        ergebnis = ergebnis + (zahl * zahl)
        #ergebnis = ergebnis + pow(zahl,2)
    return ergebnis


eingabe= input("Gib eine positive Zahl ein: ")
print(summeDerQuadrate(int(eingabe)))
