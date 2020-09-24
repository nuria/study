#!usr/local/bin

# destination is n levels up
# we can take from 1 to k events at a time
# this really needs to return 0
# if there is not a possibility

def steps(n,k):
    print " {0}  {1}".format(n, k)
    _s = 0
    if n == 1 :
        _s = 1
    elif k == 1:
        _s = n
    elif n <= 0:
        _s = 0
    else:
        # now common case
        for i in range(1, k+1):
            _s+= steps(n-i,k)

    print _s
    return _s



if __name__=="__main__":
    print steps(4,2)
