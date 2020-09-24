#!usr/local/bin/python
# return all prime integers between 1 and i
import unittest
import sys
import math

# sieve of eratostones is an ancient algorithm to find all primes bigger than a number
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes


def erastotenes(n):
    # primes are defined as numbers bigger than 1
    # to make indexing easy we add zero and 1 to array as false
    primes  = []

    for i in range(0, n+1):
        primes.append(1)

    # now reset  0,1,2
    primes[0] = 0
    primes[1] = 0
    primes[2] = 1

    for j in range(2, n+1):
        # has j index been flipped to 0?
        if primes[j] == 0:
            next
        else:
            # now flip all numbers that are multiples of j
            for k in range(j*2, n+1):
                if k % j == 0:
                    primes[k] = 0
    return primes


def brute_force_is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0 and n!=i :
            return False
    return True

def is_prime(n, exclusion_list):
    # we need to memoize something
    # if we exclude the multiples of primes
    prime = False
    for i in range(4, n):
        # first test if multiple of a prime
        multiple = False
        for j in exclusion_list:
            if i % j == 0:
                multiple = True
        # if it is not multiple of a prime does that imply it is prime?
        if not multiple:
            exclusion_list.append(i)
            prime  = True
    return (prime, exclusion_list)

def primes(a):
    # brute force , divide every integer n  by 2 to sqrt(n)
    # if we exclude the multiples of primes
     exclusion_list = [2,3]

     for i in range(4, a):
        (prime, exclusion_list) = is_prime(i , exclusion_list)

     return exclusion_list

if __name__=="__main__":
    a = int(sys.argv[1])

    print primes(a)

    prime_list = []

    for i in range(2, a):
        if brute_force_is_prime(i):
            prime_list.append(i)
    print prime_list

    prime_indexes = erastotenes(a)
    for k in range(0, a+1):
        if prime_indexes[k] == 1:
            print k

