'''
Perfekte Zahlen
'''

for i in range(2,100000):
    perfekteZahl=0
    for j in range(1, (i//2)+1):
        if(i%j==0):
            perfekteZahl += j
        if perfekteZahl>i:
            break
    if(perfekteZahl==i):
        print("Perfekte Zahl: ", perfekteZahl)
