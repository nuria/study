#!/usr/local/bin

# number of rings
# if you know how to transfer n -1 rings how does that help
A = [ 'L', 'M', 'S', 'XS']
B = []
C = []

target = C

source = A


# no represents the bottom most item we want to move
def move(n , source, target, auxiliary):

    if n > 0:
        move(n-1, source , auxiliary, target)

        target.append(source.pop())

        print (A, B, C)

        move(n-1, auxiliary, target, source)


print (A, B, C)
move(len(A), A, B,C)
