def translate(list1):
    s=""
    for i in list1:
        if i in d:
            s+=d[i]
            s+=" "
    return s

d={"merry":"god", "christmas":"jul", "a    nd":"och", "happy":"gott", "new":"nytt", "year":"år"}
print (translate(input().split()))
