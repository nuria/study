#/usr/local/bin

def main():
    D =['bad','cot','dog', 'dag','dot','cat']
    s = 'cat'
    t = 'dog'

    # treat strings as nodes on an undirected graph with an edge between them
    # if they differ in one char

    # graph
    # each entry is an array of edges
    # with the right representation this is a BFS
    G = {}
    v = {}
    print (D)

    for n in D:
        G[n] =[]
        v[n] = 0

    # building the grap is o(n2) if we do not do something smarter
    for w in D:
        # compare with the rest of the words
        # set intersection
        for w2 in D:
            if w ==w2:
                continue
            difference = 0
            # same functionality using set intersection
            #if len(set(w2).intersection(w)) >= 2:
            #     G[w].append(w2)
            for c in w2:
                if c not in set(w):
                    difference+=1
            if difference < 2:
                G[w].append(w2)



    print (G)
    
    import collections as c 
    q = c.deque([])
    q.append(s)

    path = 0
    # BFS
    while len(q) > 0:
        node = q.popleft()
        v[node] = 1
        path +=1
        if node == t:
            # this would be the shortest sequence
            print(path)
            return
        else:
            for g in G[node]:
                if v[g] < 1:
                    q.append(g)

        print(q)
    # no path
    print("-1")

if __name__=="__main__":
    main()
