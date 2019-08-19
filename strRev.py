

def strRev(s):
    
    i=-1
    revstr=''
   # j=((-1)*len(s))
    while i>=((-1)*len(s)):
        revstr+=s[i]
        i-=1
    return revstr

s=input()
print(strRev(s))

