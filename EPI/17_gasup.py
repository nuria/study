#!usr/local/bin/python


class Node:
    def __init__(self, distance_next_city, distance_you_can_cover, _next = None):
        self.distance_next_city = distance_next_city
        self.distance_you_can_cover = distance_you_can_cover
        self.next = _next


def find_ample(gas, distance_next_city):

    print "distance to next city"
    print distance_next_city

    cities = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']
    distance_next_city = [0] + distance_next_city
    gas = gas + [0]

    print  " gas"
    print gas





    distance = []
    tank = 0

    for i in range(0, len(distance_next_city)):

        if i != 0:
            distance = distance + distance_next_city[i]
        else:
            distance  = distance_next_city[i]


        if i != 0:
            tank_at_arrival = tank - distance_next_city[i]/20
            tank = tank - distance_next_city[i]/20  + gas[i]
            print cities[i]
            print "{0} {1}".format(distance, tank_at_arrival)
        else:
            tank = gas[i]

        print "({0}, {1})".format(distance, tank)






if __name__=="__main__":

    cities = [900, 600, 200, 400, 600, 200, 100]
    gas = [50, 20, 5, 30, 25, 10, 10]

    find_ample(gas, cities)
