#!usr/local/bin
# do not use heapdict to keep track of users with most events
# return top-n users ordered by amount of events
# but also keep track of quantity
# order alphabetically if there is a tie


import unittest


def topN(_input, N):
    users = {}
    
    users_events = {}

    # add user if we have not see it 
    # per user we keep the total ops and we also have a reverse lookpup from ops to users
    for (u, amount) in _input:
        if users.get(u) is None:
            users[u] = 0
            users_events[u] = 0

        users[u] += amount
        users_events[u] += 1

    # we can get all keys and values for ops and sort that list 
    l = []
    for k in users_events.keys():
        l.append((k, users_events[k]))

    # now sort this list by number of events but also if there is a tie
    # mutiply by -1 so we can sort descending order on number of events 
    # but ascending on names
    top_n = sorted( l, key=lambda x: (x[1]*(-1),x[0]) )
    
    top_n_w_balance = []
  
    for t in top_n:
        top_n_w_balance.append( (t[0], users[t[0]]) )

    return top_n_w_balance[0:N]
    





class TestSuite(unittest.TestCase):
    def test_happy(self):
        _input = [("user1", 1), ("user2", 34), ("user3", 4), ("user3",67), ("user4", 78), ("user5", 2), ("user1", 34), ("user5", 67)]
        self.assertEqual(topN(_input, 2), [("user1", 35), ("user3", 71)])

if __name__=="__main__":
    unittest.main().result


