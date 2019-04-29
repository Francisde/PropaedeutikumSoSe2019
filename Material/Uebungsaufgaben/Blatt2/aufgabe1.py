'''
gewichtete Quersumme
'''

def gewichteteQuersumme(n):
    position=1
    summe=0
    while(n>0):
        letzteZiffer=n%10
        n= n//10
        summe=summe +(letzteZiffer*position)
        position=position +1

    return summe

print(gewichteteQuersumme(5687))
