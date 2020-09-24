#!usr/local/bin

def rectangle(xl, yl, xu, yu):
    # we keep track of all points that make the perimeter
    # and this works for rectangles other than the ones fully contained on the other
    points = []

    # from xl, yl to xl
    for i in range(xl, xu):
        points.append((i, yl))

    for j in range(yl,yu):
        points.append((xu,i))

    for k in range(xu, xl,-1):
        points.append((k,yu))

    for n in range(yu,yl, -1):
        points.append((xl,n))

    return points

if __name__=="__main__":
    # rectangles are

    # build array of points for two rectanges

    points1 = rectangle(2,1, 4,4)
    points2 = rectangle(-1,-1,3,4)

    common = set(points1) & set(points2)
    print common
