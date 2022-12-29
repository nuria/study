#!/usr/local/bin
import sys
import copy

from collections import deque


WIDTH = 6 # seven units, zero indexing

# trying to code https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/17.py
# after understanding what is happening
def get_piece (y, i):
    piece_1 = set( [(2,y), (3,y), (4,y), (5,y)])
    piece_2 = set([(3,y), (2,y +1),(3, y+1), (4, y+1), (3, y+2)]) 
    piece_3 = set( [(2,y), (3,y), (4,y), (4, y+1),(4,y+2)])
    piece_4 = set([(2, y), (2,y+1), (2, y+2), (2, y+3)])
    piece_5 = set([(2,y), (3,y), (2, y+1), (3, y+1)])

    pieces = [piece_1, piece_2, piece_3, piece_4, piece_5]
    return pieces[i % len(pieces)]

def move(move, piece, board):
    global WIDTH 
    moved_piece = piece 

    if move==">":
        moved_piece = map(lambda p: ( p[0] +1, p[1]), piece)
        # see if we have hit the wall
        for p in moved_piece:
            if p[0] > WIDTH:
                return piece
        #print "move right"
    else:
        moved_piece= map(lambda p:(p[0]-1, p[1]), piece)

        for p in moved_piece:
            if p[0] < 0:
                return piece
        #print "move left"
    
    if len(set(moved_piece).intersection(board))==0:
        return moved_piece
    else:
        return piece


def down(piece, board):
    # see intersection
    # if it is zero then decrement y
    down_piece = set(map(lambda p: (p[0], p[1]-1), piece ))

    for p in down_piece:
        if p[1] <0 :
            return (piece, False)

    if len(down_piece.intersection(board)) == 0:
        #print "down"
        return (down_piece, True)
    else:
        return (piece, False)

def print_board(board, height):
    global WIDTH
    row = ['.' for i  in range(0, WIDTH+1)]
    B = [copy.copy(row) for i in range(0, height+1)]
    # now add places taken
    for p in board:
        (x, y) = p
        
        #print "x: {0}, y:{1}".format(x,y)
        B[y][x] = "#"

    txt = ''
    for y in range(height, -1, -1):
        for x in range(0, WIDTH +1):
            #print "x: {0}, y:{1}".format(x,y)
            txt = txt + B[y][x]
        txt = txt +  "\n"
    print txt


def get_piece_top_height(piece):
    return max(map(lambda x: x[1], piece))


def main():
    global WIDTH
    f = open(sys.argv[1])
    
    moves = []
    _input = None
    for l in f:
        _input= l.strip()
    
    moves  = list(_input)
    print moves

    
    NUM_ROCKS =  2022  # zero indexing
    h = -1
    n = 0
    jet = 0

    PILE = set() 
    board = set()

    while n <NUM_ROCKS:
        h = h + 4  # 3 spaces above the last ocupied level, so we spawn at the 4th unocopied level? 
        # (need to check if last piece of floor counts)
        # get rock
        p = get_piece(h, n)
        n = n + 1 
        print "-----"
        while True: # move down indefinitely 
            #print "piece: {0}".format(p)
            m = moves[jet % len(moves)]    
            jet = jet + 1
            #print "move : {0}".format(m)
            (p) = move(m, p, board)
            (p, can_move) = down(p, board)
            if not can_move:
                break
            h = h -1
        # done moving, add piece to board
        board = board.union(p)
        top_height = get_piece_top_height(board)
        h = top_height
        #print "adding piece: {0}".format(p)
        #print "height: {0}".format(h)
        #print_board(board, h)
    
    print "final board"
    print_board(board, h)

    print "height (zero index)"
    print h







            



if __name__=="__main__":
    main()
