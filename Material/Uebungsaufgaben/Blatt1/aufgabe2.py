"""
Lösung zur Aufgabe 2 von Blatt 1
"""
from math import pi


def baumstammvolumen(l , d):
    ergebnis= pi/4
    ergebnis= ergebnis * pow(d,2)
    ergebnis= ergebnis * (l/10000)
    return ergebnis

def logVolume(diameter, length):
    return pi / 4 * pow(diameter, 2) * length / 10000

eingabe= input("Gib die Länge des Baumstammes ein: ")
l = int(eingabe)
eingabe = input("Gib den Durchmesser des Baumstammes ein: ")
d= int(eingabe)

print("Das Volumen des Stammes beträgt: ", baumstammvolumen(l,d))
print("Das Volumen des Stammes beträgt: ", logVolume(d, l))
