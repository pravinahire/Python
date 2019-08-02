def is_palindrome(st):
    i=0
    l=len(st)-1
    while(i<l):
        if st[i]!=st[l]:
            return False
        i+=1
        l-=1
    return True

print(is_palindrome(input()))

