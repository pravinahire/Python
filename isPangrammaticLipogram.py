


def isPanagrammaticLipogram(s):
    
    s=s.lower()
    s=list(s)
    ns=[]
    count=0

    for i in s:
        if ord(i)>=97 and ord(i)<=122 :
            if i not in ns:
                ns.append(i)
                count+=1
    
    if count==26:
        print("Panagram")
    elif count==25:
        print("Panagrammatic Lipogram")
    else:
        print("Not a Panagram , may be Lipogram")

s=input()
isPanagrammaticLipogram(s)


