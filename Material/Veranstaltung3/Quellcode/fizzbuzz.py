"""
Beispielcode zu dem FizzBuzz Programm aus der letzten Veranstaltung.
Das Programm geht alle Zahlen von 0 - 100 durch
Ist die Zahl durch 3 teilbar wird Fizz ausgegeben
Ist die Zahl durch 5 teilbar wird Buzz ausgegeben
Ist die Zahl durch 3 und 5 teilbar wird Fizzbuzz ausgegeben.
"""

def fizzbuzz():
    for zahl in range(101):
        if zahl %3 == 0 and zahl % 3 == 0:
            print(zahl, " FizzBuzz")
        elif(zahl %3==0):
            print(zahl, " Fizz")
        elif(zahl %5==0):
            print(zahl, " Buzz")


fizzbuzz()               
