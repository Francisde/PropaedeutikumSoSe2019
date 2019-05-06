"""
Methode die prüft ob ein Element in einer übergebenen Liste Liste
"""

def isIn(element, mylist):
    for i in mylist:
        if element == i:
            return True
    return False

liste=[1,3,2,"asd",True,["geschachtelte Liste"]]

print(isIn(2, liste))
print(isIn(False, liste))

# Listen können in Python alle Datentypen auch gemischt enthalten. Eine Liste kann auch sich selbst enthalten, so können Listen rekursiv aufgebaut werden
liste2=[1,2,3,4]
liste2.insert(2,liste2)
# In der Print anweisung werden rekursiv geschachtelte Listen durch ... angegeben, da die Aufzählung unendlich sein würde
print(liste2)
