"""
Funktion zur Bestimmung des Absolutbetrags einer Zahl
Beispiel für die if Funktion
"""

def absolutbetrag(zahl):
    if(zahl>=0):
        return zahl
    else:
        ergebnis = 0 - zahl
        return ergebnis

# Ausführungsbeispiel:

print("Betrag von 25: ", absolutbetrag(25))
print("Betrag von -12: ", absolutbetrag(-12))
