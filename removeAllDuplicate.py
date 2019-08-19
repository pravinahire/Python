

def removeAllDuplicates(s):

    ns=''
    for i in s:
        if i not in ns:
            ns+=i
    return ns

s=input()
print(removeAllDuplicates(s))

