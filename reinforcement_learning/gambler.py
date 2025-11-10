#! /opt/nflx/python
"""
See some code here: https://github.com/JaeDukSeo/reinforcement-learning-an-introduction/blob/master/chapter04/GamblersProblem.py

Chapter 4: https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf
A gambler has the opportunity to
make bets on the outcomes of a sequence of coin flips. If the coin comes up
heads, he wins as many dollars as he has staked on that flip; if it is tails, he
loses his stake. The game ends when the gambler wins by reaching his goal
of $100, or loses by running out of money. On each flip, the gambler must
decide what portion of his capital to stake, in integer numbers of dollars.

Modeling: undiscounted, episodic Markov Decision Process (MDP)
state is the gamblers capital, which 
can take values from [0, 99] 
and the actions are the stakes which are from [0 to min(s, 100-s)]

the reward is zerto on all transitions except in those on which the 
gambler reaches its goal

Policy: mapping from levels of capital to stakes 

the optimal policy reaches the goal the fastest

"""

import random as r
import matplotlib.pyplot as plt
import numpy as np

HEAD = 1
TAILS = 0


GOAL = 100 # also defines the number of states 
states = [i for i in range(0, GOAL+1)]

# for now all rewards are zeros
rewards = [0 for i in range(0, GOAL+1)]
# the only state with reward is the last one
rewards[GOAL] = 1

# all possible actions for a given state
actions = {}

actions[0]= []

for s in states[1:]:
    # if state is 95 the possible actions are 1,2,3,4,5, betting anything larger than 5 
    # sets you further away from the goal
    # now if state is 10 beting 10 might make sense so possible bets are [1, 2, 3..10]
    actions[s] = [i for i in range(1, min(s, GOAL-s)+1)]


policy = [0 for i in range(0, GOAL + 1)]

def play_game():
    delta = 0
    n = 0
    while True and n <10000:
        n = n + 1
        p_h = 0.4  # so prob of winning is smaller than lossing

        # build probablity table
        for s in states[1:GOAL]:
            action_rewards = []
            _actions = actions[s]
            
            for _a in _actions:
                # this is for a given state, we calculate the reward of all possible actions
                action_rewards.append(p_h * rewards[s + _a] + (1-p_h)* rewards[s-_a])
            new_reward = max(action_rewards)
            delta = abs(rewards[s] - new_reward)
            
            rewards[s] = new_reward
       

            policy[s] = actions[int(np.argmax(action_rewards))]

            if delta > 0 and delta <1e-5:
                break
            
play_game()

print(rewards)
print(policy)
    



