

def max1sInBinaryStr(s):

    s=s.split('0')
    max=len(s[0])
    i=1
    while  i<len(s):
        if len(s[i])>max:
            max=len(s[i])
        i+=1
    return max


s=input()
print(max1sInBinaryStr(s))



