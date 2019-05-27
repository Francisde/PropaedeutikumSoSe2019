# Die Liste mit 1 Mio Zahlen ist in der Datei zahlen.txt gespeichert

# Funktion revList aus Aufgabe 3
def revList(liste):
    i=0
    j=len(liste)-1
    while(i<j):
        temp=liste[i]
        liste[i]=liste[j]
        liste[j]=temp
        i +=1
        j -=1

# Öffnen der Datei zum lesen
readObject = open("zahlen.txt","r")
eingabe=[]
for line in readObject:
    # wandle die aktuelle Zeile in einen int um und füge die Zahl in die Eingabe Liste
    aktuelleZahl = int(line)
    eingabe.append(aktuelleZahl)

# invertiere die Liste
revList(eingabe)

# Öffne Ausgabe zum schreiben
writeObject = open("ausgabe.txt","w")
for zahl in eingabe:
    # die Zahl muss in eine String umgewandelt werden und ein newLine angehängt werden
    writeObject.write(str(zahl)+"\n")
