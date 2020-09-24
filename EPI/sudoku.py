#!usr/local/bin

def print_board(b):
    print "-----"
    for i in range(0 , len(b)):
        print " ". join(b[i])
    print "----"

def sudoku_solve(board):
    # print_board(board)
    M = board
    numbers=  ['1', '2', '3', '4', '5','6', '7', '8','9']
    EMPTY = '.'

    def get_current_square(row_index, column_index):
        square = []
        if row_index < 3:
          if column_index < 3:
            for i in range(0, 3):
              for j in range(0,3):
                if M[i][j] != EMPTY:
                  square.append(M[i][j])

        elif column_index < 6:
          for i in range(3, 6):
            for j in range(3,6):
              if M[i][j] != EMPTY:
                square.append(M[i][j])
        else:
          for i in range(6, 9):
            for j in range(6,9):
              if M[i][j] != EMPTY:
                square.append(M[i][j])

        return square

    def get_current_column(column_index):
        column = []
        for i in range(0, 9):
            if M[i][column_index] != EMPTY:
                column.append(M[i][column_index])
        return column

    def solve_partial_sudoku(board, row_index, column_index):
        taken = get_current_square(row_index, column_index) + filter(lambda x : x in numbers, board[row_index]) + get_current_column(column_index)
        #print taken
        taken = set(taken)

        if len(taken) == 9:
            # all numbers taken
            print_board(board)
            print "return false"
            return False

        import random
        random.shuffle(numbers)
        for n in numbers:
            if n not in taken:
                # o(NM) copy
                new_board = [r[:] for r in board]
                new_board[row_index][column_index] = n
                sudoku_solve(new_board)


    row_index = None
    column_index = None

    # row
    for i in range(0, 9):
        # column
        for j in range(0,9):
            if board[i][j] == EMPTY:
                row_index = i
                column_index = j
                solve_partial_sudoku(board, i, j)

    if row_index is None and column_index is None:
        # solved
        print_board(board)
        print "SOLVED"
        return True

if __name__ == "__main__":

    board = [\
    ["5","3","4",".","7",".",".",".","."], \
    ["6",".",".","1","9","5",".",".","."],\
    [".","9","8",".",".",".",".","6","."],\
    ["8",".",".",".","6",".",".",".","3"],\
    ["4",".",".","8",".","3",".",".","1"],\
    ["7",".",".",".","2",".",".",".","6"],\
    [".","6",".",".",".",".","2","8","."],\
    [".",".",".","4","1","9",".",".","5"],\
    [".",".",".",".","8",".",".","7","9"]]

    sudoku_solve(board)





