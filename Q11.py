def generate_n_chars(n,char):
    res=""
    for i in range(n):
        res+=char
    return res


n=int(input())
char=input()
if len(char)==1:
    print (generate_n_chars(n,char))
else:
    print("invalid char")
