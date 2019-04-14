"""
Beispielprogramm zur Nutzung der Forschleife
"""

# erstes primitives Beispiel. Printet 10 mal Hello World
def beispiel():
    for i in range(10):
        print("Hello World!")

# Funktion zur berechnung der Summe von 0 bis zahl
def gaussum(zahl):
    ergebnis= 0
    for i in range(zahl+1):
        ergebnis = ergebnis + i
    return ergebnis


print("Summe von 0 bis 100: ", gaussum(100))
