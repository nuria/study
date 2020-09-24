#usr/local/bin


def integer_sq_root(n):

    # brute force
    # square root of n is -ad most- equal to n
    """
    for i in range(1,n):
        candidate = i * i
        if candidate == n:
            return i
    """
    # serach space is [1,n]

    U = n
    L =1

    while U >=L:
        middle = (U+L)/2
        candidate = middle* middle

        if candidate == n:
            return middle
        elif candidate > n:
            # move back
            U = middle -1
        else:
            L = middle + 1



    return -1

"""
input:  x = 7, n = 3
output: 1.913
error: 0.001
"""
def real_sq_root(n, error_budget):
    # brute force would be doing an integer search to narrow down bet ween n and n+1 and
    # after incrementing between those two integers in terms of error budget
    # we can also do binary search

    # only works for n > 1 if n <1 U should be 1
    U = n
    L = 0

    while U-L > error_budget:

        middle = (U + L)/2

        candidate = middle * middle

        if  abs(candidate - n) <= error_budget:
            return middle
        elif n-candidate > error_budget:
            # candidate is too small
            # move forward
            L = middle + error_budget
        else:
            # move back
            U = middle - error_budget
    return U-L


if __name__=="__main__":
    # compute square root
    print integer_sq_root(625)
    print real_sq_root(625, 0.001)

    print real_sq_root(23, 0.001)


