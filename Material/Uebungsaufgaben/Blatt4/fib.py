# Fibonacci-Zahlen Def: fib(0)=0, fib(1)=1, fib(n)=fib(n-1)+fib(n-2)

# Funktion, welche die n-te Fibonacci Zahl rekursiv berechnet
def fibRec(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibRec(n-1) + fibRec(n-2)

# Funktion, welche die Fibonacci Zahlen imperativ berechnet
def fibImp(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1

    zahl1=0
    zahl2=1
    ergebnis=1
    count=2
    while(count<n):
        count +=1
        zahl1=zahl2
        zahl2=ergebnis
        ergebnis=zahl1+zahl2
    return ergebnis


print(fibRec(20))
print(fibImp(20))
