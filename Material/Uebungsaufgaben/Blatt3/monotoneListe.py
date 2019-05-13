def areCorrectData(data):
    if(not(type(data)==list)):
        return False
    for element in data:
        if not(type(element)==float or type(element)==int)    :
            return False
    return True

def monoton(mylist):
    if(not(areCorrectData(mylist))):
        return False
    currentMin=mylist[0]
    for element in mylist:
        if(element>=currentMin):
            currentMin=element
        else:
            return False
    return True


print(monoton((1,3,4,5,6)))
