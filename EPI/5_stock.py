#!usr/local/bin
import sys
import ast
import unittest

def brute_force(a):
   # outer loop runs n-1 times
   # inner loop  goes through n -i
   #
    outcomes = []
    for i in range(0, len(a)-1):
        # buy at day [i]
        outcome = []
        outcome.append('Buy:' + str(a[i]))

        for j in range(i, len(a)):
            outcome.append(a[j] - a[i])

        outcomes.append(outcome)

    max_outcomes = []
    for o in outcomes:
        max_outcomes.append([o[0], max(o[1:])])

    return max_outcomes

def compute_max_profit(a):
    outcomes = []

    for i in range(0, len(a)-1):
        # buy at day [i]
        outcome = []
        for j in range(i, len(a)):
            outcome.append(a[j] - a[i])

        outcomes.append(outcome)

    max_outcomes = []
    for o in outcomes:
        max_outcomes.append(max(o))

    return max(max_outcomes)

def divide_and_conquer(a):
    # divide array in half and calculte the max of each half
    if len(a) == 2:
        return a[1] -a[0]
    elif len(a) == 3:
        return compute_max_profit(a)

    first = a[0:len(a)/2]
    second = a[len(a)/2:len(a)]

    # let's do the case where the max can be found by buying in
    # one arry but selling on the other one
    # must be the max(second) -min(first)

    candidate_max_both_arrays = max(second) - min(first)

    return max(candidate_max_both_arrays, divide_and_conquer(first), divide_and_conquer(second))

def in_place(prices):
    profit = 0
    local_min = prices[0]

    for p in prices[1:]:
        if profit < p-local_min:
            profit = p-local_min
        if p < local_min:
            local_min = p


    return profit


class testing(unittest.TestCase):
    def test_in_place(self):
        a = [310,315,275,295,260,270,290,230,255,250]
        self.assertEqual(in_place(a), 30)

    def test_divide_and_conquer(self):
        a = [310,315,275,295,260,270,290,230,255,250]
        result = divide_and_conquer(a)
        self.assertEqual(result,30)

    def test_divide_and_conquer_last_element(self):
        a = [310,315,275,295,260,270,290,230,255,250,1000]
        result = divide_and_conquer(a)
        self.assertEqual(result,770)



if __name__=="__main__":
    #a = ast.literal_eval(sys.argv[1])
    # python 5_stock.py '[310, 315,275,295,260,270,290, 230,255, 250]'
    # buy at 260 sell at 290

    # create len(a) series with profits
    #max_outcomes = brute_force(a)
    #print max_outcomes

    #print divide_and_conquer(a)
    unittest.main().result


