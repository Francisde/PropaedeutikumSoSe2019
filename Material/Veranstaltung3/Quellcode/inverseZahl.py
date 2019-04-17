"""
Beispielprogramm aus der Veranstaltung zum Berechnen der inversen Zahl zu einer Usereingabe
"""

def inverseZahl(zahl):
    if(zahl !=0):
        return 1/zahl
    else:
        print("Die Zahl  darf nicht null sein")
        return ""


# Das Programm läuft in einer Endlosschleife bis der User es beendet

while(True):
    eingabe=input("Gib eine Zahl oder \"ende\" ein: ")

    if(eingabe=="ende"):# wenn der User Ende eingibt, wird das Programm beendet
        break

    zahl=int(eingabe)
    print(inverseZahl(zahl))
