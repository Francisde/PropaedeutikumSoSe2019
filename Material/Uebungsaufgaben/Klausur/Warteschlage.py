# Klasse Warteschlage
class Warteschlange:
    #Konstruktor bekommt ein maximum übergeben
    def __init__(self, maximum):
        self.queue=[] # initialisiere die Warteschlange als leere Liste
        self.maximum=maximum

    # ein neues Element soll in die Warteschlange eingefügt werden, solange die Maximalanzahl nicht erreicht ist.
    def addElement(self, newElement):
        if(len(self.queue)<self.maximum):
            self.queue.append(newElement)
        else:
            print("Fehler! Warteschlage ist bereits voll! Element \"",newElement,"\" kann nicht eingefügt werden.")
    # Soll das erste Element der Warteschlage zurückgeben und aus der Warteschlage entfernen
    def nextElement(self):
        result = self.queue.pop(0) # Funktion pop(0) liefert das erste Element und entfernt es aus der Queue
        return result

    # soll die aktuelle Warteschlage als String zurückgeben
    def __str__(self):
        result = "Die aktuelle Warteschlage: "+str(self.queue)+"\nEs ist noch Platz für " + str(self.maximum-len(self.queue)) + " Elemente"
        return result

# Test
testQueue = Warteschlange(3) # erstelle eine Warteschlage die maximal 3 Elemente aufnehmen kann.
print(testQueue)
testQueue.addElement(10)
testQueue.addElement(25)
print(testQueue)
print("nextElement: ",testQueue.nextElement())
print(testQueue)
testQueue.addElement(74)
testQueue.addElement(42)
testQueue.addElement(69)
print(testQueue)
