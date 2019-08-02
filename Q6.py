def sumOfList(list1):
    var=0
    for i in list1:
        var+=i
    return var

def mulOfList(list1):
    var=1
    for i in list1:
        var*=i
    return var


list1=list(map(lambda x: int(x), input().split(" ")))
print (sumOfList(list1))
print(mulOfList(list1))
