#!usr/local/bin/python


# design an algorithm that takes as input an array and  a number,
# and determines if there are three entries in the array (not necessarily distinct)
# that add up to the give number

def _3sum(A, total):
    # what would be a greedy strategy?
    # bad sum entries
    A.sort()
    result = []
    for i in range(0,len(A)):
        _sum = total-A[i]
        # now look progresively through the other two values

        k = 0
        j = len(A) -1
        while j-k >= 0:
            print " i:{0} j :{1} K:{2}".format(i, j, k)
            candidate = A[k] + A[j]
            if candidate > _sum:
                j = j-1
            elif candidate < _sum:
                k = k + 1
            else:
                # found!
                return (A[i], A[k], A[j])




if __name__=="__main__":

    print _3sum([11,2,5,7,3], 21)
