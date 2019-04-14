"""
Beispielprogram für die Nutzung von Formatierung in der Print Funktion
"""

kommazahl1= 12.0123
kommazahl2= 1.0195

# Beachte, dass nur die ersten beiden Nachkommastellen ausgegeben werden.
# Die zweite Zahl wird automatisch durch Python gerundet.
print("Kommazahl1: %4.2f" %(kommazahl1))
print("Kommazahl2: %4.2f" %(kommazahl2))


zahl1 = 1234
zahl2 = 13

# Bei Ganzahlen wird in der Ausgabe korrekt rechtsbündig formatiert.
print("Zahl1: %4d" % (zahl1))
print("Zahl2: %4d" % (zahl2))


# Es gibt noch viele weitere Möglichkeiten zur Formatierung.
# Bei Interresse siehe zum Beispiel bei: https://www.python-kurs.eu/python3_formatierte_ausgabe.php
