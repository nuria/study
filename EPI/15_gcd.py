#!usr/local/bin/python

def GCD(x,y):
    # the idea is that if y> x
    # the GCD of x and y is the GCD of x and y -x

    if y == x:
        return y

    if y > x:
        return GCD(x, y-x)
    else:
        return GCD(x-y, y)





if __name__=="__main__":

    print GCD(100,10)

    print GCD(17,31)

