#!usr/local/bin
import sys

lines = list(open(sys.argv[1]))

balls = map(lambda x: int(x), lines[0].strip().split(','))


print balls

boards = []

b = []

D = {}
i = 0
j = 0
B = 0

for k in range(2, len(lines)):
    # boards have 5 rows: 1..6 8..13
    if lines[k].strip() =='': 
        boards.append(b)
        b = []
        B = B + 1
        i = 0
        continue 
    # reading line
    items = map(lambda x: int(x),lines[k].split()) 

    # store in dict num by num
    for j in range(0, len(items)):
        num = items[j]
        if D.get(num) is None:
            D[num] = []
        D[num].append((B,i,j))
    
    b.append(items)
    i = i +1

    

boards.append(b)
#print boards
    
#print D

# given a board figure out if one row or column is marked '-1' for all nums meaning its sum is -5
ALL_MARKED =  -5
def is_winner(B):
    # check rows
    for i in range(0, 5):
        if sum(B[i]) == ALL_MARKED:
            return True
    # check columns
    for i in range(0, 5):
        total = 0
        for n in range(0, len(B)):
            total = B[n][i] + total
        if total == ALL_MARKED:
            return True
    return False




# start game

# draw ball 

k = 0
stop = None
winning_boards_balls = []
winning_boards = {}

while (k < len(balls)):
    ball = balls[k]
    # get position
    if D.get(ball) is not None:
        positions  = D[ball]
        while(len(positions) > 0):
            B,i,j = positions.pop()
            board = boards[B]
            board[i][j] = -1
            if is_winner(board) and winning_boards.get(B) is None:
                winning_boards[B] = 1
                winning_boards_balls.append((ball,B))
            # if all boards won stop playing
            if len(winning_boards.keys()) == len(boards):
                stop = True
                break
    if stop:
        break
    k = k + 1
    
print "winning_boards"
print winning_boards_balls

(ball, board_index) = winning_boards_balls.pop()
board = boards[board_index]

print board

# calculate sum of winner
tally = 0
for b in board:
    for n in b:
        if n !=-1:
            tally = tally + n

print ball

print tally

print ball * tally








