"""
Lösung zur Aufgabe 1 aus Blatt 1
"""

def grundumsatzMale(m, l, t):
    ergebnis = 66.47 + 13.7*m + 5*l - 6.8*t
    return ergebnis

def grundumsatzFemale(m, l, t):
    ergebnis = 655.1 + 9.6*m + 1.8*l -4.7*t
    return ergebnis

eingabe=input("Gib das Körpergewicht ein: ")
m = int(eingabe)
eingabe=input("Gib die Körpergröße ein: ")
l= int(eingabe)
eingabe=input("Gib das Alter ein: ")
t = int(eingabe)

print("Der zugehörige Grundumsatz für Männer beträgt: ", grundumsatzMale(m,l,t))
print("Der zugehörige Grundumsatz für Frauen beträgt: ", grundumsatzFemale(m,l,t))
