#!usr/local/bin

rectangles = []


def area(A):
    print A
    # super duper tonto
    global rectangles

    # find max
    tallest = max(A)


    # how many tallest together there are?
    # since we cannot sort we just have to walk the array
    # o(n)
    count = 0
    max_count = 0

    for i in range(0, len(A)):
        if i==0 and A[i]== tallest:
            count = 1
            max_count = 1
        elif A[i] == tallest and A[i-1] == tallest:
            count = count + 1
        elif A[i] == tallest :
            count = 1
        else:
            # no tallest match
            if count > max_count:
                max_count = count

    print "{0} {1}".format(tallest, max_count)

    _area = tallest * max_count

    rectangles.append(_area)

    # substract 1 if we can
    if tallest > 1:
        def substract(x):
            if x == tallest:
                return x-1
            return x

        A_prima = map(substract  ,A)
        area(A_prima)


def



if __name__=="__main__":
    # A array representing heights of adjacent buildings of  witdth=1
    # strategies finding teh talles rectangle or widest recentagle do not work
    A = [1,4,2,5,6,3,2,6,6,5,2,1,3]
    area(A)
    print rectangles
    print max(rectangles)

