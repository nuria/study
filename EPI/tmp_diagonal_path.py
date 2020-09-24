# coding: utf8
#/usr/local/bin/python
# coding : utf-8
import sys


"""

input:  n = 4

output: 5 # since there are five possibilities:
          # “EEENNN”, “EENENN”, “ENEENN”, “ENENEN”, “EENNEN”,
          # where the 'E' character stands for moving one step
          # East, and the 'N' character stands for moving one step
          # North (so, for instance, the path sequence “EEENNN”
          # stands for the following steps that the car took:
          # East, East, East, North, North, North)
Constraints:


 [
 [x, x, x, 0]
 [x, x, x, 0]
 [x, x, 0, 0]
 [x, 0, 0, 0]
 ]

you can only go E or N

"""

def num_of_paths_to_dest(n):
    # building this solution
    # the DP way
    # building a matrix although we are just going to use half
    DP= [ [0] * n  for i in range(0,n +1)]

    # building it out explicitily

    # i is E
    # j is N
    #DP[i][j]



    DP[n-2][n-2] = 1
    DP[n-1][n-2] = 1


    for i in range(n -1,-1, -1):
        for j in range(n-3, -1, -1):
            if i >= j:
                sol = []
                # movement "down" or "west" is allowed
                if i+1 >= j and i < n-1:
                    solution_west = DP[i+1][j]
                    DP[i][j] = DP[i+1][j]

                if i >= j + 1:
                    DP[i][j] =DP[i][j] +  DP[i][j+1]

    print DP
    return DP[0][0]



if __name__=="__main__":
    print num_of_paths_to_dest(int(sys.argv[1]))

