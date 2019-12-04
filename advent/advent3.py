#!usr/lib/python
import sys

# this from U6 to D7
# will enter all the intermediate points
# in a way transforming this 2D problem in a 1D one

def move_to_x_y(move, x, y):
    path = []
    distance = int(move[1:])

    if move[0] == "U":
        # x is same
        for i in range(1, distance + 1):
            path.append((x,y+i))
    elif move[0] == "R":
        # x changes , y remains
        for i in range(1, distance +1):
           path.append((x+i,y))
    elif move[0] == "L":
        for i in range(1, distance +1):
            path.append((x-i, y))
    elif move[0] == "D":
        for i in range(1, distance + 1):
            path.append((x,y-i))
    return path


def transform(c_raw):
    path = []
    x0 = 0
    y0 = 0

    for i in  range(0, len(c_raw)):
        path = path +  move_to_x_y(c_raw[i],x0,y0)
        last_point = path[len(path)-1]
        x0 = last_point[0]
        y0 = last_point[1]

    return path

if __name__=="__main__":

    f = open(sys.argv[1])

    c1_raw = f.readline().strip().split(",")
    c2_raw = f.readline().strip().split(",")

    c1 = transform(c1_raw)
    c2 = transform(c2_raw)

    #print c1
    #print c2

    intersections = set(c1) & set(c2)


    #print c1
    #print c2

    print intersections

    steps = map (lambda x : (c1.index((x[0], x[1])) +1 + c2.index((x[0],x[1]))+1), intersections)

    print min(steps)

    # remove point (0,0)

    #print intersections

    # manhattan distance is teh sum of the absolute differences of the cartesian coordinates
    # one point is (0,0) and the other the one common to both paths
    intersections_distance = map( lambda x: abs(x[0])+abs(x[1]), intersections)

    print min(intersections_distance)
