def histogram(list1):
    for i in list1:
        print ("*"*i)

list1=list(map(lambda x:int(x),input().split()))
histogram(list1)
