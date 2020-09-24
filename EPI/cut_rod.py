#!usr/local/bin

"""

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
"""

P = {}
P[0] = 0
P[1] = 1
P[2] = 5
P[3] = 8
P[4] = 9
P[5] =10
P[6] =17
P[7] = 17
P[8] =20


def cut_rod(n,Q = {}):
    # calculate maximun price , not the lengths
    # reduce steps of problem

    if n == 0:
        return 0

    if Q.get(n):
        return Q[n]

    _max = float('-inf')

    for l in range(1, n + 1):

        price = P[l] + cut_rod(n-l, Q)

        if price > _max:
            _max = price

    Q[n] = _max

    return _max




if __name__=="__main__":
    print cut_rod(8)

