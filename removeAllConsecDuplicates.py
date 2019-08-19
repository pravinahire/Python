

def removeAllConsecDuplicates(s):

    ns=''
    i=0
    while i<len(s):
        j=i+1
        ns+=s[i]
        while j<len(s) and s[j]==s[i]:
            j+=1
        i=j
    return ns

s=input()
print(removeAllConsecDuplicates(s))

