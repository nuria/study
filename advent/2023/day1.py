#!/usr/local/bin

def main():
    
    f = open('./input1.txt')

    tally = 0

    DIGITS = ('0','1','2', '3','4','5','6','7','8','9')
    
    LETTERS = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}


    for l  in f:
        chars = list(l)
        first = None
        last = None
        

        for c in chars:
            if first is None: 
                if c in DIGITS:
                    first = c
            elif c in DIGITS:
                last = c

        if last is None:
            last = first 

        if first is not None and last is not None:
            tally = tally + int(first+last)

        #print (l.strip())
        #print("{0} {1}".format(first,last))

    print(tally)
    

if __name__=="__main__":
    main()



