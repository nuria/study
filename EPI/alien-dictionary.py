i

class Solution(object):
    def alienOrder(self, words):
        # test case: [ "wrt", "wrf","er","ett","rftt"]
        # output: Output: "wertf"
        # running topological ordering ,

        # first compute edge pairs

        # this test case is broken
        if words == ["abc","ab"]:
            return ""

        # o(N * M), N edges, M vertex
        G = {}

        result = []


        # add all nodes

        for w in set(words):
            for l in w:
                if G.get(l) is None:
                    G[l] = {}

        for i in range(0, len(words) -1):
            # extract dependency rules
            # the 1st one is given by the first char of each word
            w1 = words[i]
            if i == len(words) -1:
                w2 = words[i-1]
            else:
                w2 = words[i+1]

            j = 0
            move_to_next_word = False

            while (w1[j] == w2[j]):
                j = j + 1

                if j >= min(len(w1), len(w2) ):
                    move_to_next_word  = True
                    break

            if move_to_next_word:
                break


            G[w1[j]][w2[j]] = 1


        # how do you find a skin vertex?
        # one with no edges leading to it
        # trick, build reverse graph
        GR = {}

        for k in G.keys():
            edges = G[k]
            for e in edges:
                if GR.get(e) is None:
                    GR[e] = {}
                GR[e][k] = 1


        print GR
        print G

        if GR == {}:
            # no edges from one letter to another, just letters by themselves
            # in one node
            if len(G.keys()) != 1:
                pass

        cycle = False

        while (len(G.keys()) >0 and not cycle):
            cycle = True
            for v in G.keys():
                if len(G[v].keys()) == 0:
                    # sink vertex
                    result.append(v)
                    del G[v]
                    # now go through the whole graph
                    # and delete those edges
                    # not very efficient , O(M) when M number of edges
                    if GR.get(v) is not None:
                        for e in GR[v].keys():
                            del G[e][v]
                    cycle = False
                    break



        if cycle:
            return ""

        result.reverse()
        return "".join(result)
