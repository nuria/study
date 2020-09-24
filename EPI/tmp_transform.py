#!usr/local/bin


import collections
import string
# we are left with seeing whether there is a path on the graph from
# s to t

# we use the dictionary as a graph seeing if there is a next word
# we do not build the graph per se

def production_sequence(s, t, D):
    path = []
    # FIFO , we need to popLeft
    q = collections.deque()

    q.append(s)
    del(D[s])

    letters = list(string.ascii_lowercase)

    path.append(s)
    while len(q) > 0:
        w = q.popleft()
        if w == t:
            return path

        # now figure out 'adjacent' nodes
        for i in range(0, len(w)):
            for l in letters:
                new_word = w[0:i] + l + w[i+1:]
                #print new_word
                if new_word in D:
                    del(D[new_word])
                    path.append(new_word)
                    q.append(new_word)

    return []


if __name__=="__main__":

    D = {'bat':1, 'cot':1, 'dog':1, 'dag':1, 'dot':1, 'cat':1}
    s ='cat'
    t = 'dog'

    print production_sequence(s, t, D)
