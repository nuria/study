#!usr/local/bin

# non attacking placements of n queens on
# an n x n dashboard
result = []
# for possibilities
P = [0,1,2,3]

import copy

def queens(n):

    # the representation is a strange one, we just represent columns
    # rather than 2 dimensions so we turn the problem in one that
    # is unidimensional

    def is_diagonal(i, j):

        abs(i-j)


    # we represent [0, -, -, -, -] a queen in the column
    # number 0
    # we cannot add another column that is zero
    # we keep on trying other numbers

    def queens_helper(n, sol = list()):
        # reducing to add items to a set with a set of constrains
        if len(sol) == n:
            return sol

        print sol

        for item in P:
            if len(sol) > 0:
                if item not in sol and not is_diagonal(sol[:][-1], item):
                    s = sol[:]
                    s.append(item)
                    queens_helper(n, s)
            else:
                s = sol[:]
                s.append(item)
                queens_helper(n, s)


    return queens_helper(n)

if __name__ =="__main__":
    print queens(4)

