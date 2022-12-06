#!usr/bin

import sys

"""
    [N]     [C]     [Z]
[Q] [G]     [V]     [S]         [V]
[L] [C]     [M]     [T]     [W] [L]
[S] [H]     [L]     [C] [D] [H] [S]
[C] [V] [F] [D]     [D] [B] [Q] [F]
[Z] [T] [Z] [T] [C] [J] [G] [S] [Q]
[P] [P] [C] [W] [W] [F] [W] [J] [C]
[T] [L] [D] [G] [P] [P] [V] [N] [R]
"""
def main():
    #_input0 = sys.argv[1]
    _input1 = sys.argv[1]
    """
    l1 = ['Z','N']
    l2 = ['M','C','D']
    l3 = ['P']
    """
    l1 = ['T','P','Z','C','S','L','Q','N']
    l2 = ['L','P','T','V','H','C','G']
    l3 = ['D','C','Z','F']
    l4 = ['G','W','T','D','L','M','V','C']
    l5 = ['P','W','C']
    l6 = ['P','F','J','D','C','T','S','Z']
    l7=  ['V','W','G','B','D']
    l8 = ['N','J','S','Q','H','W']
    l9 = ['R','C','Q','F','S','L','V']

    S = []
    S.append([0])
    # first row is empty, index starts at 1
    # bit ridiculous

    S.append(l1)
    S.append(l2)
    S.append(l3)
    S.append(l4)
    S.append(l5)
    S.append(l6)
    S.append(l7)
    S.append(l8)
    S.append(l9)

    f = open(_input1)

    for l in f:
        #  move 1 from 2 to 1
        l = l .strip()
        print l
        (_txt, how_many, _txt,_from, _txt, _to) = l.split() 
        print "{0}, from:{1}, to:{2}".format(how_many, _from, _to)
        how_many  = int(how_many)
        _from = int(_from)
        _to = int(_to)
        tmp =[]
        for i in range(0, how_many):
            item = S[_from].pop()
            tmp.append(item)
        
        tmp.reverse()

        for t in tmp:
            S[_to].append(t)

        print S


    print S
    txt = ''
    for i in range(1, len(S)):
        txt = txt + S[i].pop()

    print txt 




if __name__=="__main__":
    main()
