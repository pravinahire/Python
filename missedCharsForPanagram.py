def missingCharsToMakePanagram(s):

    s=s.lower()
    s=list(s)
    ns=[]
    for j in range(26):
        ns.append(-1)

    for i in s:
        if ord(i)>=97 and ord(i)<=122 :
            ns[ord(i)-97]=i
    print(ns)
    k=0
    ms=''
    while k<len(ns):
        if ns[k]==-1:
            ms=ms+(chr(97+k))
        k+=1
    print(ms)
            


s=input()
missingCharsToMakePanagram(s)


