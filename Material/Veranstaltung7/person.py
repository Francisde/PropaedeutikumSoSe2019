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

    def __str__(self):
        return self.vorname+" "+self.name+"\nAlter:"+str(self.getAlter())

peter= Person("Peter", "Müller", 1990)

print(peter)
print(peter.getAlter())
print(peter.toString())
Person.getAnzahlPersonen()
