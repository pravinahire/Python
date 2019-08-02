# Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construc    t available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good     exercise.)

def my_max(a, b):
    if a>=b:
        return a
    else:
        return b

a,b=map(lambda x:int(x), raw_input().split(' '))
print my_max(a,b)
