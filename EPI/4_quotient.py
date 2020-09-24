#!usr/local/bin

def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """

    x = abs(dividend)
    y = abs(divisor)
    # try to computwe 2^K* y < x
    # quotient add 2^k *y
    # find largest K and keep on decrementing

    k = 32

    factor = y << k

    while factor > x:
        k = k-1
        factor = y << k

    # found biggest K such 2^k *y < =x

    quotient = 0


    while (k >0 and x >=y ):
        quotient += 1 << k
        x = x - factor
        k = k -1
        factor = y << k


    quotient+=1

    # need to deal with sign:


    # first case both positive of both negative
    if ((x == dividend) and (y == divisor)) or ((x!= dividend) and (y!= divisor)):
            return quotient
    else:
        # one of the inputs is negative
        return quotient - (quotient + quotient)


if __name__=="__main__":
    # should return 3
    print divide (10, 3)

    # should return 2
    print divide(7, 3)

    # should return 1
    print divide(-1, -1)


