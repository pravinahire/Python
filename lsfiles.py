

import sys

def lsfiles(pat,flist):
     for i in flist :
         for j in pat:
           for k in i:
               if j==k :
                   
                if (i.find(pattern))!=-1:
                 print(i)




if __name__ == "__main__":

    fp=open(sys.argv[1],"r")
    flist =fp.readlines()
    lsfiles(sys.argv[2],flist)
