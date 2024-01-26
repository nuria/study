#!/usr/local/bin
import random
# place n queens in a chess board
# no recursion, finding optimun placement with random initialization

# returns matrix with a possible placement but not sure it will be optimum
def place(n):
    
    T = []
    for k in range(n):
        row = [0] * n
        T.append(row)


    

    # each item on result is teh column , rows are implicit 
    # so [1] is really row[0] column[0]
    # [1,2] is row 1 position 1, row 2 position 2
    result = []


    # we mark placement of the queens by a 1

    
    def _print(T):
        for r in T:
            print(r)

        print("___")


    def mark_attack(i,j):
        T[i][j] = 1

        for k in range(n):
            T[i][k] = 1
        

        for k in range(n):
            T[k][j] = 1
        

        # now diagonals
        r = i + 1  
        c = j + 1
        while r < n and c < n:
            T[r][c] = 1
            r = r +1
            c = c + 1

        r = i -1
        c = j - 1
        while r >= 0  and c >=0:
            T[r][c] = 1
            r = r -1
            c = c - 1

        # now diagonals
        r = i + 1  
        c = j - 1
        while r <n and c >= 0:
            T[r][c] = 1
            r = r +1
            c = c- 1

        r = i - 1
        c = j + 1
        while r >=0   and c <n:
            T[r][c] = 1
            r = r -1
            c = c + 1
        
        #_print(T)


    # m = the row
    def _calculate():

        max_queens_placed = 0
        
        configuration = None

        for r in range(100):
            result = []
            # try 10 iterations
            i = random.randint(0,n-1)
            j = random.randint(0,n-1)

            result.append(j+1)
            mark_attack(i,j)
            
            
            # this is iterative rather than recursive
            # a solution, likely not optimum
            
            queens_placed = 0

            for row in range(1,n):
                for j in range(n):
                    if T[row][j] == 0:
                        queens_placed += 1
                        result.append(j+1)
                        mark_attack(row,j)
                        break
           
            print(result)

            if queens_placed > max_queens_placed :
                max_queens_placed = queens_placed
                configuration = result[:]
            
        
        print(configuration)
        print(max_queens_placed)

    _calculate()



place(4)
