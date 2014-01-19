#!/usr/local/bin/python
import xor;
import sys;


# see: http://travisdazell.blogspot.com.es/2012/11/many-time-pad-attack-crib-drag.html
# token will be the encoding of frequent text like " the " (spaces included)
# output will be what we get of xoring the "_ the_" with the given text at
# each position of given cipher text

# returns a string padded with zeroes of length 'l'
def makeZeroPad(l):
    pad =""
    for i in range(0,l):
        pad = pad + "0";
    return pad;


def main():
    print "About to xor"

    c1 = sys.argv[1];
    token = sys.argv[2];
    ltoken = len(token);

    token = token.decode("hex");

    # token will be shorter, pad with 0 until len of c1
    l = len(c1) - ltoken;

    for i in range(0,l):
        _c1 = c1[i:i+ltoken]
        result = xor.strxor(_c1.decode("hex"),token);
        print " i = "+ str(i)
        print result
        #print result.encode("hex")

if __name__ == "__main__":
    main();
