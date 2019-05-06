"""
Beispiel zum Unterschied in der Verwendung von Referenz- und Primitivdatentypen
"""

# Integer sind primitive Datentypen zahl2=zahl1 kopiert den Wert von zahl1 in die Variable zahl2
zahl1=10
zahl2=zahl1

#die Anweisung zahl2=25 ändert deshalb nur die Variable zahl2
zahl2=25
print("Zahl1: ", zahl1)
print("Zahl2: ", zahl2)

# Listen sind Referenzdatentypen liste2=liste1 kopiert nicht die Elemente sondern nur die Adresse von liste1
liste1=[1,2,3,4,5]
liste2=liste1

# Die Anweisung liste2[1]=25 ändert die hinter der Referenz abgelegte Liste. Die Änderung gilt daher für liste1 und liste2
liste2[1]=25
print("Liste1: ",liste1)
print("Liste2: ",liste2)

# Da hier in der Funktion ein Referenzdatentypen übergeben wird ist kein return notwendig. Der Wert ist trotzdem in der Ursprungsliste geändert
def verdoppeln(mylist):
    for i in range(len(mylist)):
        mylist[i]=mylist[i]*2

verdoppeln(liste2)
print("Liste1: ",liste1)
print("Liste2: ",liste2)
