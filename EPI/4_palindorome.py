#!usr/local/bin
import sys
import math

def is_number_palindrome(n):
    # loop through
    number_of_digits = math.floor(math.log10(n)) + 1

    while (number_of_digits>2):
        print n
        number_of_digits = math.floor(math.log10(n)) + 1
        mask = math.pow(10,number_of_digits-1)
        last = n % 10
        first = int(n/mask)

        print "last:{0}, first: {1}".format(last, first)
        if last!= first:
            return False

        n = n - last*math.pow(10,(number_of_digits -1))
        n = int(n/10)

    return True


if __name__=="__main__":
    n = int(sys.argv[1])
    print is_number_palindrome(n)
