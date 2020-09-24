#!/usr/local/bin

# write the "words" that correspond to a given phone number
# example 227 669 6 corresponds to ACRONYM and ABPOMZN

import copy

d = {0:['0'],1:['1'], 2:['A', 'B', 'C'], 3:['D', 'E', 'F'],
     4:['G', 'H', 'I'], 5:['J', 'K', 'L'], 6:['M', 'N', 'O'],
     7:['P', 'Q', 'R', 'S'], 8:['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}


# phone is a list of numbers
# try to write it recursive

def memonics(phone):
    if len(phone) == 0:
        return []
    if len(phone) == 1:
        return d[phone[0]]

    else:
        # len 2 or greater
        left = d[phone[0]]
        right = memonics(phone[1:])

    words = []
    for l in left:
        for r in right:
            words.append(l+r)

    return words


MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def phone_memonic(phone_number):
    def phone_memonic_helper(digit):
        if digit == len(phone_number):
            result.append(''.join(partial_memonic))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                partial_memonic[digit] = c
                phone_memonic_helper(digit +1)




    result = []
    partial_memonic = [0] * len(phone_number)

    phone_memonic_helper(0)

    return result


if __name__== "__main__":
    #print memonics([2,2])
    #print phone_memonic('22')
    #print memonics([2,2,7,6,6,9,6])
    print phone_memonic('2276696')
