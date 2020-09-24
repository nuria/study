#!usr/local/bin/python

# find smallest element in a cyclically sorted array
def smallest_element(a):

    if len(a)==1:
        return a[0]
    elif len(a) ==2:
        return min(a[0], a[1])
    # divide array in half
    middle = len(a)/2

    first = a[0:middle]
    second = a[middle:len(a)]

    first_min = None
    second_min = None

    if first[0] < first[len(first)-1]:
        first_min = first[0]
    else:
        first_min = first[len(first)-1]


    if second[0] < second[len(second)-1]:
        second_min = second[0]
    else:
        second_min = second[len(second)-1]

    if second_min < first_min:
        return smallest_element(second)
    else:
        return smallest_element(first)


if __name__== "__main__":

    # find the samllest element of  acyclically sorted array
    a = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368 ]
    print smallest_element(a)

