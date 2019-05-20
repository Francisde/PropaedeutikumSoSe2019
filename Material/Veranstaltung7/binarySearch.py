def binarySearch(liste, request):
    if(type(liste) ==list and type(request)== int):
        return binarySearchALGO(liste, 0, len(liste)-1, request)
    else:
        return -1

def binarySearchALGO(liste, links, rechts, request):
    if(rechts-links<0):
        return -1
    haelfte=rechts-links//2
    if(liste[haelfte]==request):
        return haelfte
    elif(liste[haelfte]<request):
        return binarySearchALGO(liste, haelfte+1, rechts, request)
    else:
        return binarySearchALGO(liste, links, haelfte-1, request)


liste=[1,2,3,4,5,6,7]
for i in liste:
    print(binarySearch(liste , i))
print(binarySearch(liste , 10))
