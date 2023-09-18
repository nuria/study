#!/usr/local/bin
import sys



def main():
    s = "abc"
    haystack = "holaabcholabca"
    # try to find permutations of string s
    # on string haystack

    # we can move string s to a set 
    # o(n) in space and time + o(nlogn) => sort
    # if there are duplicates in S this does not work and it needs to be a hashmap
    letters = sorted(set(s))

    N = len(letters)

    # loop through string t and everytime we find a match see if the next N letters
    # once converted to a sorted set match our sorted set
    
    result =0

    for i in range(0, len(haystack)):

        if haystack[i] in letters:
            if sorted(set(haystack[i:i+N])) == letters:
                print (haystack[i:i+N])
                result += 1
    


    print ("there are {0} permutations".format(result))

if __name__=="__main__":
    main()
