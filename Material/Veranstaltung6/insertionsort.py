def getMinimum(mylist):
  minimum=mylist[0]
  minindex=0
  for i in range(len(mylist)):
    if(mylist[i]<minimum):
      minimum=mylist[i]
      minindex=i
  return minindex

def insertionsort(mylist):
  sortedList=[]
  while(not(len(mylist)==0)):
    minindex=getMinimum(mylist)
    sortedList.append(mylist[minindex])
    mylist.pop(minindex)
  return sortedList



liste=[3,2,1]

print(insertionsort(liste))        
