def translate(string):
    res=""
    for i in string:
        if i not in ['U','O','I','E','A','u','o','i','e','a',' ']:
            res+=i+'o'+i
        else:
            res+=i
    return res


string=input()
print (translate(string))
