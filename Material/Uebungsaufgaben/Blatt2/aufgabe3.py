'''
Fakultätemp
'''

def fakultaet1(n):
    if(n==0 or n==1):
        return 1
    ergebnis=1
    for i in range(1,n+1):
        ergebnis = ergebnis *i

    return ergebnis

def fakultaetRec(n):
    if(n==0):
        return 1
    else:
        return n* fakultaetRec(n-1)

def fakultaet2(n):
    if(n==0 or n==1):
        return 1
    zaehler=2
    ergebnis=1
    while(zaehler<=n):
        ergebnis *=zaehler
        zaehler +=1
    return ergebnis

for i in range (50):
    if(fakultaet1(i)==fakultaet2(i)==fakultaetRec(i)):
        print(True)
    else:
        print(False)
