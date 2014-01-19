#!/usr/local/bin/python

import sys
import bitstring
import virtualenv

# snipet given in coursera crypto course
# note xor of 11 and 001  will be 11, chops the last '1' at the longer string

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])



def random(size=16):
    return open("/dev/urandom").read(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    print
    print c.encode('hex')
    return c

def _main():
    key = random(1024)
    ciphertexts = [encrypt(key, msg) for msg in MSGS]

#returns raw ascii codes (decimal)
def getAscii(text):
    asciiText = ''
    for ch in text:
        asciiText = asciiText+" "+ str(ord(ch))

    return asciiText

# assumes input is a hex string, decides it before doing an xor
def main():
    ct1 = sys.argv[1];
    ct2 = sys.argv[2];

    # let's xor all strings together and see what we get
    _next = strxor(ct1.decode("hex"),ct2.decode("hex"));

    print getAscii(ct1.decode("hex"));

    print getAscii(ct2.decode("hex"));

    # print everything with ascii codes

    print _next.encode("hex");

    print _next

'''
When the Python interpreter reads a source file, it executes all of the code found in it. Before executing the code, it will define a few special variables. For example, if the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value "__main__". If this file is being imported from another module, __name__ will be set to the module's name.
'''

if __name__ == '__main__':
        main()

