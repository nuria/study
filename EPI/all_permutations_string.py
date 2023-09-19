#!/usr/local/bin

import sys

def main():
    

    def permutations(text):
        result = []
        s = list(text)
        
        if len(s) == 1:
            return s
        elif len(s) == 2:
            return [s[0]+s[1], s[1]+s[0]]

        for i in range(0, len(s)):
            if i == 0:
                perm = permutations(s[1:])
            elif i == len(s)-1:
                perm = permutations(s[0:len(s)-1])
            else:
                perm = permutations(s[0:i]+s[i+1:])
            
            #print ("for {0} these are perms {1}".format(s[i], perm))

            for p in perm:
                result.append(s[i]+p)

        return result

    
    print (permutations(sys.argv[1]))


if __name__=="__main__":
    main()
