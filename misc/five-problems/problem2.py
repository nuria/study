#!/usr/local/bin/python
'''
Write a function that combines two lists by alternatingly
taking elements. For example: given the two lists [a, b, c] and [1, 2, 3],
the function should return [a, 1, b, 2, c, 3]

Invoque like: python problem2.py '1 2 3' 'a b c '

'''
import sys


def mix(long_list, short_list):
    result = []

    for i in range(0,len(long_list)):
            result.append(long_list[i])
            if i < len(short_list):
                result.append(short_list[i])


    return result

def main():
    l1 = sys.argv[1].split()
    l2 = sys.argv[2].split()

    print "Combining {0} {1}".format(l1, l2)

    if len(l1) > len(l2):
        print mix(l1, l2)
    else:
        print mix(l2, l1)



if __name__ == "__main__":
    main()
