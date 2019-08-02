def traditional_song(no):
    while(no>0):
        print("{0} bottles of beer on the wall, {0} bottles of beer.\n".format(no)
                ,"Take one down, pass it around,",end="")
        no-=1
traditional_song(int(input()))
