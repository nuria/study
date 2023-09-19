#! /usr/local/bin



import sys


def execute(A):

    # find all possible subarrays in an array

    def find_subarrays(B):

        if len(B) == 1:
            return B
        if len(B) == 2:
            # note solution does not contain B so we need to add it at the end
            return [[B[0]], [B[1]]]
        
        # len (B) is > 2

        result = []
        
        subsets = find_subarrays(B[1:])

        result.append(B[1:])
        result.append([B[0]])

        for s in subsets:
                result.append(s)
                result.append([B[0]]+s)

        return result

    print(find_subarrays(A))
   

if __name__=="__main__":
    execute(eval(sys.argv[1]))
