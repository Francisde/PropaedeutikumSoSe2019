def mergeSort(liste):
    if(len(liste)>1):
        haelfte =(len(liste)-1)//2
        liste1 = mergeSort(liste[:haelfte+1])
        liste2 = mergeSort(liste[haelfte+1:])
        return merge(liste1, liste2)
    elif(len(liste)==1):
        return liste



def merge(liste1, liste2):
    neueListe=[]
    while(len(liste1)>0) and (len(liste2)>0):
        if(liste1[0]<=liste2[0]):
            neueListe.append(liste1.pop(0))
        else:
            neueListe.append(liste2.pop(0))
    if(len(liste1)!=0):
        neueListe.extend(liste1)
    else:
        neueListe.extend(liste2)
    return neueListe



liste=[5,6,4,2,1,3,25]
print(mergeSort(liste))
