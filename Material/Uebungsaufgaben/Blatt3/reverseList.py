def reverseList(mylist):
    if(not(type(mylist)==list)):
        return None
    result=[]
    for i in range(len(mylist)):
        result.append(mylist[len(mylist)-i-1])
    return result

print(reverseList([1,2,3,4,5]))
