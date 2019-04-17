"""
Beispielcode aus der letzten Veranstaltung der die Funktionsweise der While Schleife zeigt
"""

# Gaussumme mit while Schleife berechnen

count=0
ergebnis=0
while(count<=100):
    ergebnis = ergebnis + count
    count=count+1

print(ergebnis)


# Beispiel für Nutzung von break und continue

count=0
ergebnis=0

while(True): # Endlosschleife
    if(count>100):
        break # Verlasse die Schleife, wenn count >100
    count=count+1
    if(count%2==0):
        continue # Springe zum Anfang wenn count gerade -> rechne nur mit den ungerade zahlen weiter
    ergebnis=ergebnis+count

print(ergebnis)


# Beispiel zum rechnen mit Kommazahlen
#  Aufpassen, da mit Kommzahahlen nicht exakt gerechnet werden kann
zahl = 1.0
while(zahl<5):
    print(zahl)
    zahl=zahl+0.2
