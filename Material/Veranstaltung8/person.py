import datetime

class Person:
    # Klassenvariable counter zählt, wie viele Personen erstellt wurden
    counter=0
    # Konstruktor der Klasse Person
    def __init__(self, name, geschlecht, gebjahr):
        self.name=name
        self.geschlecht=geschlecht
        self.gebjahr=gebjahr
        Person.counter+=1

    # Objektmethode die das Alter der Person zurückgibt
    def getAlter(self):
        now = datetime.datetime.now()
        return now.year-self.gebjahr

    # Methode wandelt das Objekt in einen String um
    def __str__(self):
        return "Name: "+self.name+"\nGeschlecht: "+self.geschlecht+"\nAlter: "+str(self.getAlter())

    # static Methode gibt den Klassencounter zurück
    def getPersonenCount():
        print("Anzahl an erstellten Personen: ",Person.counter)
        return Person.counter

    # Methode zur deep-Copy eines Person Objekts
    def copyPerson(person1):
        return Person(person1.name, person1.geschlecht, person1.gebjahr)

# KLasse Konto
class Konto:
    # Konstruktor
    def __init__(self, kontonummer, kontoinhaber, kontostand):
        self.kontonummer=kontonummer
        self.kontoinhaber=kontoinhaber # Aggregation: benutzt ein Objekt der Klasse Person
        self.kontostand=kontostand

    # Objekt Methode die den aktuellen Kontostand zurückgibt
    def getKontostand(self):
        return self.kontostand

    # Mehode zur Durchführung einer Buchung auf dem Konto
    def buchung(self, betrag):
        self.kontostand +=betrag


peter = Person("peter", "male", 1993)
hans=peter # flat-copy ! Achtung hier wird nun die Referenz kopiert, beide Variablen greiefen auf das selbe Object zu
hans= Person.copyPerson(peter) # hier deep-Copy. Jetzt existieren zwei unabhängige Objekte
print(peter)
Person.getPersonenCount()
person3=Person("Petra","female", 1980)


konto1 = Konto(12.3, hans, 0.00)
konto1.buchung(100)
konto1.buchung(-25)
print(konto1.kontostand)
print(konto1.kontoinhaber)
