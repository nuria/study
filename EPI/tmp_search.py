#!usr/local/bin

# returns the largest integer whose square is less than or equal
# to the given integer
def int_sqrt(n):
    #300 -> 17 as 17^2  = 289

    # seems that binary searchish in nature
    # if 1 ->1
    # if 2 ->1
    #16 ->4

    # square root is les than half the number, true? is this a rule
    # interval is a tutple
    # this is O(n/2) ~ o(n)
    if n  in (1,2,3):
        return 1
    # let's do it interatively rather than recursion
    right = n
    left = 0

    while left <= right:
        mid = (right + left)/2
        test_value = mid * mid

        if test_value == n:
            return mid
        elif test_value > n:
            # reduce the search_space in half
            right = mid -1

        elif test_value < n :
            # augment search space in 1
            left = mid +1

    return left



if __name__=="__main__":
    print int_sqrt(16)
    print int_sqrt(300)
