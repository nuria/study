#!/usr/local/bin

import sys

def main():

    data = []
    numbers = {}
    parts = []
    gears = {}

    EMPTY =''
    DOT = '.'
    GEAR = '*'


    def is_adjacent(x, y, max_x, max_y, num):
        adjacent = False
        candidates = []
        # north
        if y > 0:
            candidates.append((y-1,x))
        if x > 0:
            candidates.append((y,x-1))
        if y <max_y:
            candidates.append((y+1,x))
        if x <max_x:
            candidates.append((y,x+1))
        
        # diagonally might be y + 1 , x + 1
        # bottom and before
        if x > 0 and y < max_y:
            candidates.append((y+1, x-1))
        # upand before
        if x> 0 and y > 0:
            candidates.append((y-1,x-1))

        # bottom and after
        if x < max_x and y < max_y:
            candidates.append((y+1, x+1))
        # up and after
        if x < max_x and y > 0:
            candidates.append((y-1, x+1))


        for c in candidates:
            (y0,x0) = c
            p = data[y0][x0]
            if p != DOT and p not in ('1','2','3', '4','5','6','7','8','9','0'):
                adjacent = True
            # we need to loop through all
            if gears.get((x0,y0)) is not None:
                # the presence of a gear ensure this is a part
                # add to tally
                gears[(x0, y0)].append(num)

        return adjacent


    f = open(sys.argv[1])

    # we can keep track of the numbers in a hash and their coordinates
    # for each digit 
    # for each number and each set of coordinates we check noth south east west
    # but numbers might appear twice
    # hash needs to identify the 1st set of coordinates
    # so like  (467, (0,0))

    # 467..114..
    # 4,6,7,*,*, 1, 1, 4, *,*,*
    # read 


    x = 0
    y = 0

    for l in f:
        chars = l.strip()
        
        # 4,6,7, , , 1, 1, 4,  , 
        n = EMPTY
        row = []
        x = 0
        first_coordinate = None
        for c in chars:
            if c.isnumeric():
                n = n + c
                if first_coordinate is None:
                    first_coordinate = (x,y)
            else:
                if n!= EMPTY:
                    # add number to data structure
                    numbers[(n,first_coordinate)] = (first_coordinate[0], x)
                    
                    n = EMPTY
                    first_coordinate = None
            if c == GEAR:
                gears[(x,y)] = []

            row.append(c)
            x = x + 1

        # handle border
        if n!= EMPTY:
            # add number to data structure
            numbers[(n,first_coordinate)] = 1

        data.append(row)
        y = y + 1


    #print(gears)
    #print(numbers)

    # now figure out which numbers are parts
    
    max_y = len(data) -1
    max_x = len(data[0])-1

    for k in numbers.keys():
        (n, first_coordinate) = k
        (x, y) = first_coordinate
        adjacent = False

        
        #print("{0}".format(k))
        for x in range(x, x +len(n)):
            adjacent = is_adjacent(x,y, max_x, max_y, n)
            if adjacent:
                # one of the positions is adjacent , no need to check further
                break


        if adjacent and n not in parts:
            parts.append(int(n))

    #print(gears)

    tally = 0
    
    for k in gears.keys():
        num_adjacent = len( gears[k])
        if num_adjacent == 2:
            tally = tally + int(gears[k][0]) * int(gears[k][1])
    

    print(sum(parts))
    print (tally)


if __name__=="__main__":
    main()
