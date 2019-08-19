def q2(s):
    if s[0]=='k':
        print('True')
    elif s[0]=='y':
        q1(s[1:])
    else:
        q0(s[1:])


def q1(s):
    if s=='':
        print('False')
    else:
        if s[0]=='a':
            q2(s[1:])
        elif s[0]=='y':
            q1(s[1:])
        else:
            q0(s[1:])

   

def q0(s):
    if s=='':
        print('False')
    else:
        if s[0]=='y':
            q1(s[1:])
        else:
            q0(s[1:])
    

s=input()
q0(s)

