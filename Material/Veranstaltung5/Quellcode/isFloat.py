"""
Funktion die prüft, ob eine gegebener String eine Float Zahl darstellt.
Kann genutzt werden um zum Beispiel fehlerhafte Eingaben abzufangen.
"""

def isFloat(string):
    # ersetze das erste vorkommen des Dezimalpunkt durch eine 1
    string = string.replace(".", "1", 1)
    #war die Eingabe eine Float Zahl, dann enthält sie jetzt nur noch Zahlen
    return string.isdigit()

zahl=0
while(True):
    eingabe=input("Gib eine Zahl ein: ")
    if isFloat(eingabe):
        zahl = float(eingabe)
        break
    else:
        print("Das war keine gültige Zahl!")

print(int(eingabe))
