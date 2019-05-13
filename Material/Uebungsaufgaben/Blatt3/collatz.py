def collatzNachforler(n):
    if(n%2==0):
        return n/2
    else:
        return (3*n)+1

def collatzIteration():
    result=[]
    for count in range(2,10000):
        aktuelleZahl=count
        iteration=0
        while(aktuelleZahl!=1):
            iteration +=1
            aktuelleZahl=collatzNachforler(aktuelleZahl)
        print("Iterationen für ",count," : ",iteration)
        result.append(iteration)

collatzIteration()
