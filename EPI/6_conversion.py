#!usr/local/bin
import sys
import math

def get_digit(d):
    # gets the digit by comparing to 0..9
    data = {}
    data["0"] = 0
    data["1"] = 1
    data["2"] = 2
    data["3"] = 3
    data["4"] = 4
    data["5"] = 5
    data["6"] = 6
    data["7"] = 7
    data["8"] = 8
    data["9"] = 9
    return data[d]

def get_number_as_str(n):
    data = {}
    data[0] = "0"
    data[1] = "1"
    data[2] = "2"
    data[3] = "3"
    data[4] = "4"
    data[5] = "5"
    data[6] = "6"
    data[7] = "7"
    data[8] = "8"
    data[9] = "9"
    return data[n]

def str_to_int(s):
    s = list(s)
    # now we have alist of integers
    # we compose integer using powers of 10
    l = len(s)

    # if l = 3, max 10 power is 2
    n = 0
    k = l -1
    for i in s:
        n = math.pow(10,k) * get_digit(i) + n
        k = k -1

    return n


def int_to_str(n):
    s = ''
    # assuming positive
    while (n > 0):
        # 1st digit from the right
        d = n % (10)
        n = int(n/(10)
        s += get_number_as_str(d)

    return  ''.join(reversed(s))




if __name__=="__main__":
    s = sys.argv[1]
    print str_to_int(s)

    print int_to_str(int(s))
