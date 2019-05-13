def isPalindrome(mystring):
    mystring=mystring.lower()
    for count in range(len(mystring)):
        if(mystring[count]!= mystring[len(mystring)-count-1]):
            return False
    return True

eingabe = input("Gib ein Palindrom ein: ")
print(isPalindrome(eingabe))
