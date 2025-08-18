#! /opt/nflx/python


# recursive algorithm that returns 0
# or 1 if the word is found
def find_next(r, c, letter, d):
    

    # not the letter we needed, stop
    if m[r][c] != letter:
        return 0

    # we finished
    if letter == "S":
        global tally
        tally+= 1
    # keep going
    else:
        # look for next letter
        if r > 0 and d =="UP":
            find_next(r - 1, c, NEXT[letter],d)
        
        if c > 0 and d =="LEFT":
            find_next(r, c - 1, NEXT[letter],d)
        
        if c < right and d =="RIGHT":
            find_next(r, c + 1, NEXT[letter],d)
        
        if r < bottom and d == "DOWN":
            find_next(r + 1, c, NEXT[letter],d)
        # go sideways
        # up right
        if r > 0 and  c < right  and d =="UP_RIGHT":
            find_next(r - 1, c + 1, NEXT[letter],d)
        # up left
        if r > 0  and c > 0 and d =="UP_LEFT":
            find_next(r - 1, c - 1, NEXT[letter],d)

        # down right
        if r < bottom and c < right  and d =="DOWN_RIGHT":
            find_next(r + 1, c + 1, NEXT[letter],d)

        # down left
        if r < bottom and  c > 0 and d =="DOWN_LEFT":
            find_next(r + 1, c - 1, NEXT[letter],d)

        


##########################################################

# find XMAS
m = []

NEXT = {"X": "M", "M": "A", "A": "S"}
DIR = ["RIGHT", "LEFT", "DOWN", "UP" , "DOWN_RIGHT", "UP_RIGHT", "DOWN_LEFT", "UP_LEFT"]

f = open("./input4.txt")

for line in f:
    line = line.rstrip()
    out = map(lambda x: x if x in ["X", "M", "A", "S"] else ".", list(line))
    m.append(list(out))


left = 0
top = 0
bottom = len(m) - 1
right = len(m[0]) - 1

# result
tally = 0



for i in range(0, len(m)):
    for j in range(0, len(m[0])):
        for d in DIR:
            find_next(i, j, "X", d)

print(tally)
