# Die Funktion aus der Pingo Aufgabe

def recFunk(n):
    if(n%2==1):
        n = n-1
    if(n==0):
        return 0
    else:
        return n+ recFunk(n-2)

print(recFunk(7))
