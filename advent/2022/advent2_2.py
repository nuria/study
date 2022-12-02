#!usr/local/bin
import sys


TIE = 3
WIN = 6
LOSS = 0

VALUES ={'R':1, 'P':2,'S':3}

# given a value, gives you a winner choice
# so gurantees a win
WINNERS = {'R':'P', 'P':'S', 'S': 'R'}

# given a value, gives you  a looser choice
# gurantees you loose 
LOOSERS = {'R':'S','P':'R','S':'P'}

def main() :
    # pass input file
    f = open(sys.argv[1]);

    elf_plays = []
    plays= []
    score = 0

    for l in f:
        (elf, play) = l.split()
        elf = translate(elf)

        plays.append(translate2(play, elf))
        elf_plays.append(elf)

    print elf_plays
    print plays

    for i in  range(0, len(elf_plays)):
        elf_p = elf_plays[i]
        p = plays[i]
        _round = rps(elf_p,p) 
        score = score + _round
        print "score for round"
        print _round

    print "total score"
    print score


    


def translate(p):
    if  p in ('A', 'X'):
        p = 'R'
    elif p in ('B', 'Y'):
        p ='P'
    elif p in ('C','Z'):
        p ='S'
    return p



# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
def translate2(p, e):
    if p== "Y":
        p = e
    elif p=="X":
        p = LOOSERS[e]
    elif p =="Z":
        p = WINNERS[e]
    return p


# returns a score for player (not elf) after a play
def rps(elf_p, p):
    s = 0
    
    if elf_p == p:
        s = TIE
    
    elif elf_p =="R" and p not in ("P"):
        s = LOSS

    elif elf_p =="P" and p not in ("S"):
        s = LOSS

    elif elf_p =="S" and p not in ("R"):
        s = LOSS
    else:
        s = WIN

    return VALUES[p] + s






# 1st column
# A for Rock, B for Paper, and C for Scissors
# 2nd column
# Score: 1 for Rock, 2 for Paper, and 3 for Scissors
# plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won)


if __name__=="__main__":
    main()
