#Definition der Klasse StepCounter
class StepCounter:

    # Konstrukor
    def __init__(self, datum):
        self.datum=datum
        self.zaehler=0

    def incrementSteps(self):
        self.zaehler +=1

    def __str__(self):
        return "Am "+self.datum+" bin ich "+str(self.zaehler)+" Schritte gegangen"


# Test
schrittZaehler1 = StepCounter("28.05.2019")
schrittZaehler2 = StepCounter("29.05.2019")
for i in range(5000):
    schrittZaehler1.incrementSteps()

for i in range (2500):
    schrittZaehler2.incrementSteps()

print(schrittZaehler1)
print(schrittZaehler2)
