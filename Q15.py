def find_longest_word(list1):
    max1=-1
    for i in list1:
        if len(i)>max1:
            max1=len(i)
    return max1

print(find_longest_word(input().split()))
