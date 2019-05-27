
# Funktion zur Prüfung ob ein korrekter Punkt-Klammer-Ausdruck vorliegt
# liefert True oder False zurück
def checkPunktKlammerAusdruck(string):
    oeffnendeKlammern=0
    for zeichen in string:
        if(zeichen=="("):
            oeffnendeKlammern +=1
        if(zeichen==")"):
            if oeffnendeKlammern >0:
                oeffnendeKlammern -=1
            else:
                return False
    if oeffnendeKlammern==0:
        return True
    else:
        return False

# Testfälle aus der Aufgabenstellung

print(checkPunktKlammerAusdruck("()")) # muss True sein
print(checkPunktKlammerAusdruck("(()(a)(()((c))))")) # muss True sein
print(checkPunktKlammerAusdruck("")) # muss True sein
print(checkPunktKlammerAusdruck("(()")) # muss False sein
print(checkPunktKlammerAusdruck("(()())a)")) # muss False sein
print(checkPunktKlammerAusdruck(")(")) # muss False sein
