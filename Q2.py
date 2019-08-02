
def max_of_three(a, b, c):
    if a>=b:
        if a>=c:
            return a
        else:
            return c
    else:
        if b>=c:
            return b
        else:
            return c


a,b,c=map(lambda x: int(x), raw_input().split(" "))
print max_of_three(a,b,c)
