#!usr/local/bin
import sys

# this is o(2^n)
# where n is the number of bits needed to represent the base
# x ^y
# divide problems on problems of size y/2
def better_pow(y,x):
    if y == 0: return 1
    elif  y == 1:return x
    elif y >  1:
        # y is odd
        if y & 1 == 1:
            # divide by 2 the exponent
            return (x * better_pow(int(y/2),x) * better_pow(int(y/2),x))
        else:
            return (better_pow(int(y/2),x) * better_pow(int(y/2),x))

def some_pow(y,x):
    result = 1
    for i in range(0, y):
        result = result * x
    return result

if __name__=="__main__":

    x = int(sys.argv[1])
    y = int(sys.argv[2])

    print x
    print y

    print some_pow(x,y)
    print better_pow(x,y)



