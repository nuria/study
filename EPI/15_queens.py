#!/usr/local/bin

import sys

"""
sol for 4: 
[[2,4,1,3], 
 [3,1,4,2]]

 sol for 6:
 [[2,4,6,1,3,5],
 [3,6,2,5,1,4],
 [4,1,5,2,6,3],
 [5,3,1,6,4,2]]
"""


def main():

    # the representation of result 
    # is important, we are representing rows with the position in each row 
    result =[] 


    n = int(sys.argv[1])

    def place(n, p=[]):
        
        #print(f'positons:{p}')

        if n == 1:
            return [1]
        if n == len(p):
            print(p)
            return p

        if len(p) < 1:
            for i in range(1,n+1):
                place(n, [i])

        else:

            # test if a newly placed queen will conflict with the ones placed prior
            for i in range(1, n+1):
                # to figure out how to describe a diagonal is a bit hard
                # the key is to realize that row-column is constant 
                # we describe each diagonal by its invariant so row-column = 0 in the diagonals in the middle
                # of the square, the (1,10, (2,2)... 
                # len(p)+1 is the column
                # i is the row

                # once a row is taken we cannot place a queen in its row and column                
                if i not in p:
                    r = i
                    c = len(p) + 1
                    
                    #print (f'trying {i}')
                    
                    positiveDiagonals = []
                    negativeDiagonals = []
                    for (column,row) in enumerate(p):
                        column = column + 1
                        positiveDiagonals.append(row-column)
                        negativeDiagonals.append(row+column)
                        
                    #print(f'{positiveDiagonals} {negativeDiagonals}')

                    if r-c not in positiveDiagonals and r+c not in negativeDiagonals :
                        
                        #print (f'apending {i}')
                        sol = p[:]
                        sol.append(i)
                        place(n, sol)


    print(place(n, []))




if __name__=="__main__":
    main()
