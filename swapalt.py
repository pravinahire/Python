

def main():
   a = [1,2,3,4,5,6,7,87,8,9,10]
   flag = 1
#   a = input()
   for x in range(len(a)):
      if(flag==1):
        print(a[x])
        flag = -1
      else :
        flag = 1
      
main()
