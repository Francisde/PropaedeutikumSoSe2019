"""
Erstes Beispielprogramm zur Berechnung des Flächeninhalts und Umfangs
eines Rechtecks
"""

inputvar = input("Gib die Länge a ein: ")
a = int(inputvar)
inputvar = input("Gib die Länge b ein: ")
b = int(inputvar)

umfang= 2 * a + 2 * b
flaecheninhalt = a * b
print("Umfang: ", umfang)
print("Flächeninhalt: ", flaecheninhalt)
