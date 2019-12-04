#!usr/local/bin/python
import sys

cache = {}

def add_fuel(mass):

    fuel = 0
    while  (mass/3) -2  > 0:
        new_fuel = (mass/3) -2
        fuel = fuel + new_fuel
        mass = new_fuel

    return fuel

if __name__ =="__main__":

    f = open('./advent1.txt')
    total_fuel = 0

    for l in f:
        #print "calculating " +l
        total_fuel += add_fuel(int(l.strip()))

    print total_fuel
    print add_fuel(100756)
    print add_fuel(1969)

