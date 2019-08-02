import sys


def totalmarks2(line):
    name,subject,marks,total = line.strip().split('|')
    return "%s|%s|%s\n" % (name,subject,(float(marks)*100)/float(total))

def allstuds(lines):
    a=[]
    for l in lines:
        a.append(totalmarks2(l))
    return a  
    
if __name__ == '__main__':
    h=open(sys.argv[1],"r")
    lines = h.readlines()
    oh=open(sys.argv[2],"w")
    oh.writelines(allstuds(lines))
    oh.close()
    
