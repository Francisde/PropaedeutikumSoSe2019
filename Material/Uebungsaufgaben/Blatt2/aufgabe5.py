'''
Berechnung von PI
'''

def PI():
    pi=1
    for i in range(1,10000000):
        pi = pi*(((2*i)*(2*i))/(((2*i)-1)*((2*i)+1)))

    return pi*2

print(PI())
