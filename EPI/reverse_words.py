#!usr/local/bin/python
"""
You are given an array of characters arr that consists
of sequences of characters separated by space characters.
Each space-delimited sequence of characters defines a word
Implement a function reverseWords that reverses
the order of the words in the array in the most efficient manner.
"""


def reverse_words(A):
    # asuuming two spaces
    SPACE = "  "
    # with o(n) space
    import collections
    q = collections.deque()
    w = ''
    #o (n) time
    for i in range(0, len(A)):
        if A[i] == SPACE or i == len(A) -1:
            if i == len(A) -1:
                w += A[i]
            q.append(w)
            w = ''
        else:
            w += A[i]

    # drain
    # use space in A

    A = []
    # o len(words)
    while(len(q) > 0):
        w = q.pop()
        for c in w:
            A.append(c)
        A.append(SPACE)
    print A

if __name__ == "__main__":

    _input = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]


    _output = [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]

    print reverse_words(_input)

