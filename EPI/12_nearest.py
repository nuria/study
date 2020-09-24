#!/usr/local/bin/python


a = []

# find the two closest instances of the same word
def find_closest(a):
    # pairs and distance
    c = {}
    w = None
    d = len(a)
    for i in range(0, len(a)):
        item = a[i]
        if  c.get(item) is None:
            c[item] = [(0,i,0)]

        else:
            # add distance
            # add tuple (i,d) where i is the position and d distance to prior pair
            prior = c[item][-1][1]
            _d = i -prior
            c[item].append((prior, i, i-prior))
            if _d <d:
                w = item
                d = _d


    print c
    print d
    print w

if __name__=="__main__":
    a = ["All", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]
    print find_closest(a)
