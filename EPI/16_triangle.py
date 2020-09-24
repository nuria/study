#!usr/local/bin

# given a triangular structure of numbers
# find the minimun path from top to bottom
# each step you might move to adjacent numbers on the row below
# from item 21 you can rwach 31 and 32 and row 3 has ad most 3 items


def minimum_path(t):

    # calculate for a level?
    # from a given position on the level below
    # we are moving up


    def _calculate(l, p):
        # from position i in level l
        # i can reach position i and i-1 in level i -1
        # unless position i is last in which case i can only reach i-1
        # or first in which case i can only reach i
        items = t[l]

        # first level
        if l == 0:
            return items[0]
        else:

            if p == 0:
                # only one possible path
                return items[0] + _calculate(l-1,0)
            #last element on level 2 (with 3 elements) is indexed at 2
            elif p == l:
                # only one possible path
                return items[p-1] + _calculate(l-1,p-1)
            else:
                # two possible paths
                return min(items[p-1] + _calculate(l-1, p-1), items[p] + _calculate(l-1, p))


    # levels are going to be  3,2,1,0
    paths =[]
    # starting at the base
    for i in range(0, len(t[-1])):
        paths.append(_calculate(len(t)-1,i))

    return min(paths)


def dp(t):

    # only records prior row
    cache = [0] * len(t)
    tmp_cache = [0] *len(t)
    print cache
    for row in t:
        cache = tmp_cache[:]

        for j in range(0, len(row)):
            if j == 0:
                path = row[j] + cache[0]
            elif j == len(row)-1:
                path = row[j] + cache[j-1]
            else:
                path = row[j] + min(cache[j], cache[j-1])
            tmp_cache[j] = path
        print cache

    return min(tmp_cache)



if __name__=="__main__":
    # solution is  11
    print dp([[2],[3,7], [8,5,6],[6,1, 9,3]])
    print minimum_path([[2],[3,7], [8,5,6],[6,1, 9,3]])
