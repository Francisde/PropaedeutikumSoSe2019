class Spieler:

    def __init__(self, name):
        self.name=name

    def __str__(self):
        return self.name

class Spielfeld:

    def __init__(self):
        self.feld=[["","",""],["","",""],["","",""]]

    def setPice(self, spalte, reihe, currentPlayer):
        self.feld[reihe][spalte]=self.getSpieler(currentPlayer)

    def korrekteEingabe(self, spalte, reihe):
        if(spalte >=0 and spalte<3) and (reihe >=0 and reihe<3):
            if self.feld[reihe][spalte]=="":
                return True
        return False

    def getSpieler(self, currentPlayer):
        if(currentPlayer==0):
            return "X"
        if(currentPlayer==1):
            return "O"
        if(currentPlayer=="X"):
            return 0
        if(currentPlayer=="O"):
            return 1

    def gewonnen(self):
        for i in range(3):
            if(self.feld[i][0]==self.feld[i][1]==self.feld[i][2]) and self.feld[i][2] !="":
                return self.getSpieler(self.feld[i][0])
            if(self.feld[0][i]==self.feld[1][i]==self.feld[2][i]) and self.feld[2][i] !="":
                return self.getSpieler(self.feld[0][i])
        if (self.feld[0][0]==self.feld[1][1]==self.feld[2][2]) and self.feld[1][1] !="":
            return self.getSpieler(self.feld[1][1])
        if (self.feld[0][2]==self.feld[1][1]==self.feld[2][0]) and self.feld[1][1] !="":
            return self.getSpieler(self.feld[1][1])
        return -1

    def __str__(self):
        result=""
        for row in range(len(self.feld)):
            result+=self.feld[row][0]
            result+=" | "
            result+=self.feld[row][1]
            result+=" | "
            result+=self.feld[row][2]
            result+="\n--------\n"
        result+="\n"
        return result

class Spiel:

    def __init__(self, spieler1, spieler2):
        self.spieler1=spieler1
        self.spieler2=spieler2
        self.spielfeld=Spielfeld()

    def getSpieler(self, currentPlayer):
        if(currentPlayer==0):
            return self.spieler1
        else:
            return self.spieler2

    def run():
        print("Starte ein neues Spiel")
        inputString =input("Wie heißt der erste Spieler?: ")
        spieler1=Spieler(inputString)
        inputString =input("Wie heißt der zweite Spieler?: ")
        spieler2=Spieler(inputString)
        spiel = Spiel(spieler1,spieler2)
        currentPlayer=0
        print(spiel.spielfeld)
        while True:
            print(spiel.getSpieler(currentPlayer)," ist an der Reihe.")
            weiter=True
            while weiter:
                spalte= int(input("Welche Spalte wählst du aus? : "))
                reihe= int(input("Welche Reihe wählst du aus? : "))
                if(spiel.spielfeld.korrekteEingabe(spalte, reihe)):
                    weiter=False
                else:
                    print("Eingabe nicht korrekt")
            spiel.spielfeld.setPice(spalte, reihe, currentPlayer)
            print(spiel.spielfeld)
            currentPlayer= 1-currentPlayer
            if(spiel.spielfeld.gewonnen()>=0):
                print(spiel.getSpieler(spiel.spielfeld.gewonnen())," hat gewonnen")
                weiter = input("noch eine runde?: ")
                if weiter.upper()=="J":
                    currentPlayer=1
                    spiel.spielfeld=Spielfeld()
                else:
                    break

Spiel.run()
