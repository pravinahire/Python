

def secondMostFrequentChar(s):
    fcount=[]
    for i in range(52):
        fcount.append(0)
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            fcount[ord(i)-65]+=1
        elif ord(i)>=97 and ord(i)<=122:
            fcount[ord(i)-97+26]+=1

    if fcount[0]>fcount[1]:
        f=fcount[0]
        se=fcount[1]
    else:
        f=fcount[1]
        se=fcount[0]
    k=2
    while k<len(fcount):
        if fcount[k]>f:
            t=f
            f=fcount[k]
            if t>se:
                se=t
        elif fcount[k]>se:
            se=fcount[k]
        k+=1
    #print(fcount)
    finlist=[]
    j=0
    while j<len(fcount):
        if ((fcount[j])==se) and j<=25:
            finlist.append(chr(65+j))
        elif ((fcount[j])==se) and j>25:
            finlist.append(chr(71+j))
        j+=1
    print(finlist)





s=input()
secondMostFrequentChar(s)
