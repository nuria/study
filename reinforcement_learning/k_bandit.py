#!/opt/nflx/python
#import unittest
import numpy as np
import matplotlib.pyplot as plt
import time

"""
From : https://medium.com/data-science/reinforcement-learning-multi-arm-bandit-implementation-5399ef67b24b
and http://incompleteideas.net/book/RLbook2020.pdf

https://github.com/MJeremy2017/reinforcement-learning-implementation/blob/master/Multi-ArmBandit/bandit.py

Modeling for octopus with k arms playing k slot machines each of which
returns a fixed price

"""
# 
class Bandit:

    """
    K: number of slot machines
    """
    def __init__(self, k, seed=None, exploration_rate=.3, learning_rate= 0.1):
        self.k = k
        # actions are represented as numbers, each stands for the slot machine we are going to pick
        self.actions = range(self.k)
        
        # initial estimates for values are zeros
        # this array keeps the estimates for values that are updated after each action taken
        self.values = np.zeros(self.k)
        
        # the payout of each machine is a random value generated from the normal distribution
        self.true_value = []

        self.total_reward = 0
        self.avg_reward = []

        np.random.seed(seed)
        for i in range(0, k):
            self.true_value.append(np.random.rand()) 

        # these two gauge the exploit/explore ratio
        # the exploration_rate is the epsilon in the e-greedy methods
        self.exploration_rate = exploration_rate
        self.learning_rate = learning_rate
        
        # number of trials
        self.times = 0
        # number of actions for each bandit
        self.action_times = np.zeros(self.k)

    # we want to maximize the reward
    # using an e-greedy strategy, meaning that we exploit 1-e times
    def chooseAction(self):
        # draw to decide whether this is an explore or an exploit
        choice = np.random.uniform(0, 1)

        # explore
        if choice < self.exploration_rate:
            action = np.random.choice(self.actions)
        else:
            #exploit
            action = np.argmax(self.values)

        return action

    """
    Receives an action and updates estimates of that action after 
    receiving a reward
    """
    def takeAction(self, action):
        self.times += 1
        self.action_times[action]+=1 

        reward = self.true_value[action] + np.random.randn() # adds some randomness to the reward
        
        # update estimates of that action 
        # adding the difference between the current observation minus prior observation
        # mutiplied by a learning_rate
        # this is a generic formula but not k bandit specific?
        self.values[action] += self.learning_rate * (reward - self.values[action])
        
        self.total_reward += reward
        self.avg_reward.append(self.total_reward/self.times)



def play(n, k, seed):
    bandit = Bandit(k, seed)
    
    for i in range(0,n):
        action = bandit.chooseAction()
        bandit.takeAction(action)

    print (" Total reward :{0} ".format(bandit.total_reward))
    return bandit

if __name__=="__main__":
    print("playing 10 bandits, 1000 times seed 1234")
    bandit_1 = play(1000, 10, 1234)

    
    print("playing 10 bandits, 2000 times seed 678")
    bandit_2= play(2000, 10, 678)

    print("playing 10 bandits, 5000 times seed 4567")
    bandit_3 = play(5000, 10, 4567)

   # reward plot
   
    plt.figure(figsize=[8, 6])
    plt.plot(bandit_1.avg_reward, label="10 bandits,1000 plays")
    plt.plot(bandit_2.avg_reward, label="10 bandits, 2000 plays")
    plt.plot(bandit_3.avg_reward, label="10 bandits, 5000 plays")

    plt.xlabel("n_iter", fontsize=14)
    plt.ylabel("avg reward", fontsize=14)
    plt.legend()
    
    plt.show()

    time.sleep(60000)
   


        
    





