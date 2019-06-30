# Musterlösung zur Aufgabe 7

# Methode perrinZahl berechnet die Perrin Zahl zur Eingabe n
# die Methode berechnet die Perrin Zahl nicht rekursiv
def perrinZahlImp(n):
    zahlMinus3=3
    zahlMinus2=0
    zahlMinus1=2
    if(n== 0):
        return zahlMinus3
    elif(n==1):
        return zahlMinus2
    elif(n==2):
        return zahlMinus1
    else:
        counter=3
        zahlN=0
        while counter <=n:
            zahlN=zahlMinus2+zahlMinus3
            zahlMinus3=zahlMinus2
            zahlMinus2=zahlMinus1
            zahlMinus1=zahlN
            counter +=1
        return zahlN


# Methode zur rekursiven Berechnung der Perrin Zahl für Eingabe n
def perrinZahlRek(n):
    if(n== 0):
        return 3
    elif(n==1):
        return 0
    elif(n==2):
        return 2
    else:
        return perrinZahlRek(n-3)+perrinZahlRek(n-2)

def testPerrin():
    for i in range(101):
        ergebnis1=perrinZahlImp(i)
        ergebnis2=perrinZahlRek(i)
        if(ergebnis1 != ergebnis2):
            print("Fehler in der Berechnung!")
            return;
        else:
            if(i !=0 and ergebnis1 % i == 0):
                print(i)

testPerrin()
