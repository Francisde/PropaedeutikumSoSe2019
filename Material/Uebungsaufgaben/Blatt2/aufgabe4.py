'''
ggT Berechnung mit Euklid
'''

def euklid(a, b):
    while b!= 0:
        t=b
        b = a%b
        a=t
    return a

print("ggT von 16 und 12: ", euklid(12,16))
