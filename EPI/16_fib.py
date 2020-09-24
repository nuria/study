#!usr/locl/bin
# f(n) = F(n-1)+ F(n-2)

cache = {}

def fib(n):
    global cache
    if n== 0 or n==1:
        return n
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]

# how do you do this in constant time?
# you just uuse two variables fib-1 and fib_2

def fib_constant(n):
    if n <= 1:
        return n
    f_minus_2, f_minus_1 = 0, 1
    for i in range(1,n):
        f = f_minus_2 + f_minus_1

        f_minus_2 = f_minus_1
        f_minus_1  = f

    return f_minus_1


import md5


# bootstrap base case

K = {}

def maximun_sum(a):
    # let's cache per number of elements considered?
    global K
    k = "".join(str(a))


    if len(a) == 0:
        return 0
    elif K.get(k):
        return K[k]
    elif len(a) == 1:
        K[k] = a[0]
        return K[k]
    elif len(a) == 2:
        _sum = max(max(a[0], a[1]), sum(a))
        K[k] = _sum
        return K[k]
    else:
        # need to loop through all possible subarrays of a
        _max = None
        for i in range(0, len(a)-1):
            for j in (i+1, len(a)-2):
                subarray = a[i:j + 1]
                prior = maximun_sum(subarray[i:j])
                current = prior + a[-1]
                key = "".join(str(subarray))
                K[k] = max( a[-1], max(prior, current))
                if K[k] > _max or _max is None:
                    _max = K[k]

    return _max


def maximun_sum_better(A):
    max_seen  = 0
    max_end = 0

    B = [float('-inf')] * len(A)

    B[0] = A[0]

    for i in range(1, len(A)):

        B[i] = max(B[i-1] +A[i], A[i])


    print B
    return max(B)




if __name__ =="__main__":
    # o(n) in space
    # o(n) in time
    print fib(4)
    print fib_constant(4)

    a = [904,40,523,12,-335,-385,-124,481,-31]

    print maximun_sum([904, 40, 523, 12, -335, -385, -124, 481, -31])
    #print maximun_sum_better(a)
    print maximun_sum_better([-2,3,1,-7,3,2,-1])
