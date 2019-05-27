def bubbleSort(liste):
    for i in range(len(liste)):
        changes=False
        for j in range(len(liste)-1):
            if not inOrder(liste[j],liste[j+1]):
                temp=liste[j]
                liste[j]=liste[j+1]
                liste[j+1]=temp
                changes=True
        if( not changes):
            break

def inOrder(zahl1, zahl2):
    return zahl1<=zahl2

liste=[5,6,2,12,3,4,7]
bubbleSort(liste)
print(liste)
