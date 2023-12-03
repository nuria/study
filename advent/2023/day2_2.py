#!/usr/local/bin

import sys

def main():

    f = open(sys.argv[1])

    valid_games = []

    counter = 0

    # 12 red cubes, 13 green cubes, and 14 blue cubes
    RED = 12
    GREEN = 13
    BLUE = 14
    

    for l in f:
        counter = counter + 1

        # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        l = l.strip()
        turns = l.split(';')

        
        red = 0
        green = 0
        blue = 0

        for t in turns:
            # ["3 blue, 4 red", "1 red, 2 green"]

            cubes = t.split(',')
            # [3 blue, 4 red]

            for c in cubes:
                #print(c)
                [n, color] = c.split()

                if color =="red":
                    red = max(red, int(n)) 
                elif color =="blue":
                    blue = max(blue, int(n))
                elif color =="green":
                    green = max(green, int(n))


        valid_games.append(red*blue*green)


        
    print(valid_games)
    print(sum(valid_games))




if __name__=="__main__":
    main()
