#!usr/local/bin

# given a list of outcomes
# of matches among pairs of teams
# is there asequence of teams starting with A
# and ending with B such each team in the sequence has beaten the next team in the sequence?
# (A, C, 'win') and ('C', 'B', 'win')
# if we model teams as nodes and edges connect teams
# are winning games  we jaust ahve to see if there is a  direct path
# between A aand B

import collections

def direct_path(games, node1, node2):
    # build graph with team from source_vertex having beaten team with landing_vertex
    G = {}
    for g in games:
        source_vertex = g[1]
        destination_vertex = g[2]
        if G.get(source_vertex) is None:
            G[source_vertex] = []
        G[source_vertex].append(destination_vertex)

    # is there a path from node1 to node2, BFS from node1?

    # uses a FIFO queue
    d  = collections.deque()
    d.append(node1)

    current = None
    while (current != node2 and len(d) >0):
        current = d.pop()
        for n in G[current]:
            d.append(n)


    if len(q) == 0:
        return False
    else:
        return True

if __name__=="__main__":
    # data is (result, winning_team, loosing_team)
    games = []
    print direct_path(games,'A', 'B')
