import sys

def totalmarks1(line):
    name,subject,marks,total = line.strip().split('|')
    return "%s|%s|%s\n" % (name,subject,(float(marks)*100)/float(total))

def allstuds(lines):
    return [totalmarks1(l) for l in lines]

if __name__ == '__main__':
    h=open(sys.argv[1],"r")
    lines = h.readlines()
    oh=open(sys.argv[2],"w")
    oh.writelines(allstuds(lines))
    oh.close()
