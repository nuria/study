#!usr/local/bin
import unittest

# Ac for acumulator
def revenue(coins, a):
    if len(coins) == 2:
        return max(coins) + a

    else:
        # see plays for player2
        # player1 chooses left most coin
        play1 = max(coins[1], coins[-1])
        # player1 chooses right most coin
        play2 = max(coins[0], coins[len(coins)-2])

        if play1 >play2:
            # player1 should choose right most
            # to minimize next play
            return revenue(coins[0:len(coins)-2],coins[-1] +a)
        else:
            return revenue(coins[1:], coins[0] +a)


def optimal_revenue(coins):
    if len(coins) <= 2:
        return max(coins)
    #if coins[1..n]
    # if 1st player selects coins[0]
    # and second player plays optimally
    # first player will end up with
    p1 = coins[0] + sum(coins[1:]) - optimal_revenue(coins[1:])
    # now choose right most
    p2 = coins[-1] + sum(coins[0:-1]) - optimal_revenue(coins[0:-1])

    return max(p1, p2)

class Testing(unittest.TestCase):
    def test_happy_case(self):
        coins = [5,25,10,1] # resul 26
        self.assertEqual(26, revenue(coins, 0))
        self.assertEqual(26, optimal_revenue(coins))

    def test_other(self):
        coins = [25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25,1, 25, 5, 10] #solution 140
        self.assertEqual(optimal_revenue(coins), 140)


if __name__=="__main__":
    coins = [5,25,10,1] # resul 26
    coins = [10,25,5,1,10,5] #solution 31
    coins = [25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25,1, 25, 5, 10] #solution 140
    print revenue(coins, 0)
    print optimal_revenue(coins)
    unittest.main().result
