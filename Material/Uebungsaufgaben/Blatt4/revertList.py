def revList(liste):
    i=0
    j=len(liste)-1
    while(i<j):
        temp=liste[i]
        liste[i]=liste[j]
        liste[j]=temp
        i +=1
        j -=1

liste=[1,2,3,4,5,6]
revList(liste)
print(liste)
