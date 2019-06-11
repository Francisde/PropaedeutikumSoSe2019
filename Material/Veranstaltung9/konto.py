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
        self.buchungen=[]

    # Objekt Methode die den aktuellen Kontostand zurückgibt
    def getKontostand(self):
        return self.kontostand

    # Mehode zur Durchführung einer Buchung auf dem Konto
    def buchung(self, betrag):
        self.kontostand +=betrag
        self.buchungen.append(betrag)

    def getKontoAuszug(self):
        print("-----------------\nKontoauszug")
        for i in self.buchungen:
            print(i)
        print("-----------------")
        print("Aktueller Kontostand: "+str(self.getKontostand()))


class GiroKonto(Konto):

    def __init__(self, kontonummer, kontoinhaber, kontostand, dispo):
        super().__init__(kontonummer, kontoinhaber, kontostand)
        self.dispo=dispo

    def buchung(self, betrag):
        if(self.kontostand + betrag < 0-self.dispo):
            return "Zu wenig Geld!"
        else:
            super().buchung(betrag)
            return self.kontostand

class Sparbuch(Girokonto):

    def __init__(self, kontonummer, kontoinhaber, kontostand, zinssatz):
        super().__init__(kontonummer, kontoinhaber, kontostand,0)
        self.zinssatz=zinssatz



gk = GiroKonto(123, Person("Peter","male", 1990),0.00,200)
print(gk.getKontostand())
gk.buchung(100)
gk.buchung(-23.99)
print(gk.buchung(-199.99))
gk.getKontoAuszug()
