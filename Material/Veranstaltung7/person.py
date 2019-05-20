class Person:
    counter=0
    def __init__(self, vorname, name, gebjahr):
        self.vorname=vorname
        self.name=name
        self.gebjahr=gebjahr
        Person.counter+=1
    def getAnzahlPersonen():
        print("Anzahl an erstellten Personen: ",Person.counter)
    def getAlter(self):
        return 2019-self.gebjahr

    def toString(self):
        return self.vorname+" "+self.name+"\nAlter:"+str(self.getAlter())
    def __str__(self):
        return self.vorname+" "+self.name+"\nAlter:"+str(self.getAlter())

peter= Person("Peter", "Müller", 1990)

print(peter)
print(peter.getAlter())
print(peter.toString())
Person.getAnzahlPersonen()

### zeige Objecte sind referenzen
person2=peter

print(person2)
person2.name="Meier"
print(person2)
print(peter)

class Konto:

    def __init__(self, person, kontonummer, saldo):
        if(type(person)==Person and type(kontonummer)== int and type(saldo)== float):
            self.kontoinhaber=person
            self.kontonummer=kontonummer
            self.saldo=saldo
        else:
            print("keine korrekten Datentypen")

    def __str__(self):
        return "Konto: "+str(self.kontonummer)+"\nKontoinhaber: "+str(self.kontoinhaber)+"\nSaldo:"+str(self.saldo)

konto1=Konto(peter, 123, 0.00)
print(konto1)
konto2=Konto("Alf", 1234, 0.00)
