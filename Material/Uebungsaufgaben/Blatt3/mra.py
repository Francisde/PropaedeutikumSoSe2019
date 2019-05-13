def mra(mystring):
    # alle Buchstaben zu Großbuchstaben
    mystring = mystring.upper()
    mystring=entferneDoppelKonsonanten(mystring)
    mystring=entferneVokale(mystring)
    mystring=kuerzeWort(mystring)
    return mystring

def entferneDoppelKonsonanten(mystring):
    index=0
    while(index<len(mystring)):
        if(mystring[index]==mystring[index+1]):
            mystring= mystring.replace(mystring[index],"",1)
        index +=1
    return mystring

def entferneVokale(mystring):
    for vokal in ['A','E','I','O','U']:
        mystring=mystring.replace(vokal,'')
    return mystring

def kuerzeWort(mystring):
    if(len(mystring)<=6):
        return mystring
    else:
        neuerString=mystring[:3]
        neuerString=neuerString+mystring[-3:]
        return neuerString

print(mra("Basketball"))
print(mra("Programm"))
