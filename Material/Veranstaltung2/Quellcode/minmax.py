"""
Beispiel Programm zur Veranschaulichung der if-Funktion
"""

# Funktion min liefert das Minimum zweier Zahlen
def min(zahl1, zahl2):
    if(zahl1<zahl2):
        return zahl1
    else:
        return zahl2

# Funktion max liefert das Maximum zweier Zahlen
def max(zahl1,zahl2):
    if(zahl1>zahl2):
        return zahl1
    else:
        return zahl2


# Ausführungsbeispiel:
print("Maximum von 2 und 5: ", max(2,5))
print("Minimum von 2 und 5: ", min(2,5))
