class Kommazahl:
    def __init__(self, vorkomma, nachkomma):
        self.vorkomma=vorkomma
        self.nachkomma=nachkomma

    def __str__(self):
        return str(self.vorkomma)+"."+str(self.nachkomma)

    def __add__(self, other):
        self.vorkomma +=other.vorkomma
        self.vorkomma +=(self.nachkomma + other.nachkomma)//10
        self.nachkomma = (self.nachkomma + other.nachkomma)%10

zahl = Kommazahl(1,2)
zahl2 = Kommazahl(1,9)
zahl = zahl + zahl2
print(zahl)

altezahl=1.2
for i in range(10):
    altezahl +=0.2
    print(altezahl)
print("neueZahl")
zahl=Kommazahl(1,2)
for i in range(10):
    zahl + Kommazahl(0,2)
    print(zahl)
