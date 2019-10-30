#!/usr/bin/python

"""
The longest palindromic sequence on a string is the longest common subsequence
among a string (X) and its reverse (R)

Given a sequence, find the length of the longest palindromic
subsequence in it. For example,if the given sequence is BBABCBCAB,
then the output should be 7 as BABCBAB is the longest palindromic subseuqnce in it.
BBBBB and BBCBB are also palindromic subsequences of the given sequence,
but not the longest ones.

"""



"""
every single string of length 1 is a palindrome
if len(x) == 1:
    x

if first and last character are not the same

X[i] ! = X[j]:
    L[i,j] = max (L[i+1,j], L[i, j+1])

if first and last char are the same
L[i,j] = L[i+1, j-1] +2


Generalization
    c[i,j] -> the length of an LCS of sequences Xi and Yj which are prefixes of strings X and Y

    if  i or j =0 -> c[i,j] =0
    else if  Xi ==Yj -> c[i,j] = c[i-1, j-1] + 1
    else  if Xi!=Yj
        c[i,j] = max(c[i,j-1], c[i-1,j)

"""


def LCS(X,Y):
    # these list comprehensions are not defined in teh most obvious way, watch out
    c = [ [0 for i in range(len(Y)+1)] for j in range(len(X)+1)]

    for  i in range(0,len(X)):
        for j in range(0, len(Y)):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] +1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    print c
    return c[len(X)-1][len(Y)-1]

s = 'BBABCBCAB'
reverse_s = list(s)
reverse_s.reverse()

#solution is 7
print LCS('BBABCBCAB', reverse_s)

# solution is 5
print LCS('ACCGGGTTAC', 'AGGACCA')



