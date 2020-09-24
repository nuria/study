#!usr/local/bin

# n for needle
# h for hay stack

# see https://brilliant.org/wiki/rabin-karp-algorithm/
def _hash(txt):
    # using ord to produce a hash given a string
    # this hash is a rolling one
    # as it has the property that adding or substracting  a char we can create a new hash
    # in linear time
    # signature
    base = 26
    power = len(txt) -1
    s = 0
    for c in txt:
        s = ord(c) * (base ** power) + s
        power = power -1

    return s

# modify hash by removing front item and adding an item at the back
def _modify_hash(h, txt, c):
    # max order
    base = 26
    power = len(txt)-1

    # substract 1st char
    h = h - ord(txt[0]) * (base ** power)
    # shift left
    h = h * base
    # now add new char
    h = h + ord(c) * (base**0)

    return h


def rabin_karp(hs, needle):

    l_needle = len(needle)
    l_hs = len(hs)

    if l_needle > l_hs:
        return -1

    # for it to be linear requires a linear function
    h_needle = _hash(needle)
    h_haystack = _hash(hs[0:l_needle])

    if h_needle == h_haystack:
        return 0

    for i in range(0, len(hs) -l_needle):
        #advance 1
        print hs[i:l_needle]
        h_haystack = _modify_hash(h_haystack,hs[i:l_needle], hs[i+1])
        if h_needle == h_haystack:
            return i

    return  -1


if __name__== "__main__":

    print rabin_karp('abcd','cd')
    print rabin_karp('hello nu', 'ell')
