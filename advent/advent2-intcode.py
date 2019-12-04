#!usr/local/lib
import sys


def run_intcode(code, l):

    p1 = code[1]
    p2 =  code[2]
    p3 = code[3]

    if p3 > len(l):
        # invalid
        return l

    if code[0] == 1 :
        l[p3] = l[p1]  + l[p2]
    elif code[0] == 2:
        l[p3] = l[p1] * l[p2]

    return l

def run_program(k, j, l):
    l[1] = k
    l[2] = j

    # pointer
    i = 0
    while i < len(l):
        if l[i]  == 99:
            break;
        input_program = l[i:i+4]
        l = run_intcode(input_program, l)
        i = i + 4
    return l

if __name__=="__main__":
    f = open('./advent2.txt')
    original_list = f.readline().strip().split(",")
    original_list = map(int, original_list)
    # now to read the op code we need to be able to modify the list

    for k in range(0, 99):
        for j in range(0,99):
            l = run_program(k,j, original_list[:])
            print k
            print j
            print l[0]
