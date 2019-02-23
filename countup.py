#recursive function countup
#negative argument 
#counts “up” from -3 number


def countup(n):
    if n>=0:          # added if n is greater than zero 
        print ('Blastoff!')
    else:
        print(n)
        countup (n+1) # added a +1 integer to countup from n
countup(-3)
