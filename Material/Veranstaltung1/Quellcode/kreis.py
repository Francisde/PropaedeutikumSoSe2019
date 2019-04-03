"""
Beispielprogramm zur Berechnung des Flächeninhalts und Umfangs
eines Kreises bei gegebenem Radius.
Beispiel für das einbinden einer externen Library
"""

from math import pi

inputvar = input("Gib den Radius r ein: ")
radius = int(inputvar)

umfang = 2 * pi * radius
durchmesser = 2 * radius

flaecheninhalt = (pi * pow(radius, 2))/4

print("Umfang: ", umfang)
print("Flächeninhalt: ", flaecheninhalt)
