#!usr/local/bin
import random


if __name__== "__main__":
    t = 0

    requests = []
    p1 = (3, 9/18)
    p2 = (5, 6/18)
    p3 = (7, 2/18)
    p4 = (11, 1/18)

    while  (t < 1000000):
        r = random.uniform(0,1)

        # how do we do the mapping
        if r < 9/18.0:
            requests.append(3)
        elif r > 9/18.0 and r < (9/18.0 + 6/18.0):
            requests.append(5)
        elif r > (9/18.0 + 6/18.0) and r < (9/18.0 + 6/18.0 +2/18.0):
            requests.append(7)
        elif r > (9/18.0 + 6/18.0 + 2/18.0):
            requests.append(11)
        t = t + 1

    for i in requests :
        print i

