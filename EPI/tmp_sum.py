#!usr/local/bin


def pair (a, target):
    # allocate a different array
    # with solution, will be represented by two variables
    start = 0
    end = len(a)-1
    # figure out if there are two entries that add up to a third one
    # we assume array is sorted

    while start < end:
        s = a[end] + a[start]
        if (s)> target:
            # move a[end] inwards
            end = end -1
        elif s < target:
            start = start +1
        else:
            return True

    return False

# determine if 3 entries on the array, not necessarily distinct
# add up to a number
def _3sum(a, target):
    # get all pairs including self
    pairs = []
    for i in a:
        for j in a:
            pairs.append(i+j)

    items = set(a)

    # see if one of our pairs can find a third item

    for p in pairs:
        if target-p in items:
            return True

    return False

def _3sum_better(a, target):
    # sort array
    # o (nlogn)
    a = sorted (a)
    # o(n) space
    start = 0
    end = len(a) -1
    while start <= end:
        s = a[end] + a[start]
        if s  <= target:
            # we are looking
            # for target-s
            if contains(a, target-s):
                return True
            else:
                # moving on
                start = start + 1
        else:
            # sum > target
            end = end -1

    return False

def contains(a, item):

    if len(a) ==0 or (len(a) == 1 and a[0]!= item):
        return False

    middle = len(a)/2

    if item  < a[middle-1]:
        return contains(a[0:middle], item)
    elif item >a[middle-1]:
        return contains(a[middle:], item)
    else:
        return True



if __name__=="__main__":
    print pair([-2,1,2,4,7,11], 6)

    print pair([-2,1,2,4,7,11], 0)

    print pair([-2,1,2,4,7,11], 10)

    print _3sum([11,2, 5, 7,3], 21)

    print _3sum_better([11,2, 5, 7,3], 21)

