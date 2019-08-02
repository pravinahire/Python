def length(list1):
    x=0
    for i in list1:
        x+=1
    
    return x  

list1=map(lambda x: int(x), raw_input().split(" "))
print length(list1)
