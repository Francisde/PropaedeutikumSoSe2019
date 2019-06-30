import math


def solveEq(a, b ,c ,d):
    c = c-d # bring die rechte Seite der Gleichung auf 0 -> a*x^2 + b*x +c-d = 0
    d=0
    c=c/a # Gleichung normalisieren -> x^2 + b/a * x + (c-d)/a = 0
    b=b/a
    a=a/a
    # nun kann auf die Gleichung die pq Formel angewandt werden
    #berechne zuerst den inneren Term
    innererTerm= (b/2)*(b/2) - c
    if(innererTerm < 0):
        print("Die Gleichung hat keine Lösung!")
    else:
        loesung1 = (0-b)/2 + math.sqrt(innererTerm)
        loesung2 = (0-b)/2 - math.sqrt(innererTerm)
        if(innererTerm == 0):
            print("Die Gleichung hat genau eine Lösung: ",loesung1)
        else:
            print("Die Gleichung hat zwei Lösungen:\nLösung 1: ",loesung1,"\nLösung 2: ",loesung2)


print("Das Programm berechnet die Lösung der Gleichung a*x^2 + b*x + c = d\nBitte gib die Parameter ein!")
a=float(input("Parameter a: "))
b=float(input("Parameter b: "))
c=float(input("Parameter c: "))
d=float(input("Parameter d: "))
solveEq(a,b,c,d)
