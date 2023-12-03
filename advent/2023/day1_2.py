#!/usr/local/bin
import sys


def main():
    
    f = open(sys.argv[1])

    tally = 0

    DIGITS = ('1','2', '3','4','5','6','7','8','9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    
    LETTERS = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}


    for l  in f:
        first = None
        last = None
        index_of_first = float('inf')
        index_of_last = -1
        candidate = None

        s = l.strip()

        for k in DIGITS:
            # returns lowest index or -1
            first_index = s.find(k)
            last_index = s.rfind(k)
            if first_index >= 0:
                if k.isnumeric():
                    candidate = k
                else:
                    candidate = LETTERS[k]

                if first_index <= index_of_first:
                    first = candidate
                    index_of_first = first_index
                if last_index >= index_of_last:
                    last = candidate
                    index_of_last = last_index


        if first is not None:
            tally = tally + int(first+last)

        print("{0} => {1} {2}".format(l.strip(), first, last))

    print(tally)
    

if __name__=="__main__":
    main()



