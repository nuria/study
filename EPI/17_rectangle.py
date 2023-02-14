#!/usr/local/bin

import sys
def main():
    _input  = eval(sys.argv[1])

    # list is [2,1,5,6,2,3]
    # greedy
    # we can transform to [[1,2], [1], [1,2,3,4,5], [1,2,3,4,5,6], [1,2], [1,2,3]]
    # create a new list 
    buildings = []
    for i in _input:
        floors = set(range(1, i +1))
        buildings.append(floors)
            

    # now looking at all rectangles , trick is taht they have to be adjacent 
    max_height = max(_input)
    max_width = len(_input)
    max_size = 0
    

    for height  in range(1, max_height+1):
        size = 0
        i = 0
        
        while i <  max_width:
            b = buildings[i]
            
            if height in b:
                size = size + height
                if size > max_size:
                    max_size = size
            else:
                # discontinuity
                size = 0
            i = i + 1
        

    print "max_size: {0}".format(max_size)


if __name__=="__main__":
    main()
