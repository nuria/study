#!/opt/nflx/python

import copy
import pickle
import sys


"""
Markov decision processes (MDP)
grid, start at s go to +1 (win) or -1 (loose)
very similar idea to tic tac toe

# https://medium.com/data-science/reinforcement-learning-implement-grid-world-from-scratch-c5963765ebff

    -, -, -, +1
    -, -,NO, -1, 
    s, -, -, -,

Anything that cannot be changed by the agent is cosidered
to be outside of it and thus part of the environment


"""
# this positions are python matrix (row, column) = (y,x)
# is it ok to specify here the rewards for win and loose?
# seems like taht shoudl be fine as we are trying to determine the adjacent rewards?
BLOCK = (1,1)

START = (2,0)
WIN = (0,3)
LOOSE = (1,3)
BLOCK = (1,2)
MOVES = ('UP', 'DOWN','LEFT', 'RIGHT' )


# (x, y) , x E [0, 3] y E [0,2]
LEGAL_POSITIONS = []
for i in range(0, 3):
    for j in range(0,4):
        if (i,j) not in [BLOCK]:
            LEGAL_POSITIONS.append((i,j))

INITIAL_REWARD = [0,0,0,1], [0,0,0,-1], [0,0,0,0]


print(INITIAL_REWARD)


class Board:
    def __init__(self):
        # this is really current position
        self.state = START
         
    
    def nextPosition(self, action):
        _next = None
        # not sure if the position is a property of the agent or
        # the environment
        # row , column
        (y, x) = self.state 

        if action == 'UP':
            _next = (y-1, x)
        elif action == 'DOWN':
            _next = (y-1,x)
        elif action == 'LEFT' :
            _next = (y, x-1)
        else:
            _next = (y, x +1)
        if _next in  LEGAL_POSITIONS:
            return _next
        else:
            return self.state

    def isEnd(self):
        return self.state == WIN or self.state == LOOSE
    
    def printBoard(self):
        for i in range(0, 3):
            print('-----------------')
            out = '| '
            for j in range(0,4):
                if (i,j) == self.state:
                    out += 'A | '
                elif (i,j) == WIN:
                    out += '+1| '
                elif (i,j) == LOOSE:
                    out += '-1| '
                elif (i,j) == BLOCK:
                    out += 'NO| '
                else:
                    out += '  | '
            print(out)
        print('-----------------')



class Agent:
    def __init__(self, board, exp_rate, explore_rate = 0.5):
        self.states = []
        self.states_value = {}

        for s in LEGAL_POSITIONS:
            self.states_value[s] = 0.0
        # now reset the rewards for win and loose
        self.states_value[WIN] = 1.0
        self.states_value[LOOSE] = -1.0

        self.learning_rate = 0.2 # ? magic number
        self.explore_rate = explore_rate 
        self.board = board

    # balance exploit and explore
    def takeAction(self):
       
        import random
        r = random.random()
        # choose one of the moves
        if r < self.explore_rate:
           #explore
           if r <0.25:
               move =  MOVES[0]
           elif r< 0.5:
               move =  MOVES[1]
           elif r<0.75:
               move =  MOVES[2]
           else:
               move =  MOVES[3]

           next_state = self.board.nextPosition(move)

        else:
            #exploit
            # choose move with best value
            current_position = self.board.state
            next_state = None
            next_value = float('-inf')
            for move in MOVES:           
                tmp = self.board.nextPosition(move)
                if tmp in self.states:
                    # already visited this state, skip it
                    continue
                if  tmp != current_position:
                    # legal move, what is its value
                    if self.states_value[tmp] > next_value:
                        next_value = self.states_value[tmp]
                        next_state = tmp
         
        self.board.state = next_state
        
        self.states.append(next_state)




    # Vt = Vt + decay_rate * (Vt+1- Vt)
    def propagateReward(self):
        # now back propagate the rewards
        (y,x) = self.states.pop()

        reward = INITIAL_REWARD[y][x]
        for s in reversed(self.states):
           
            self.states_value[s] = self.states_value.get(s,0) + self.learning_rate * (reward - self.states_value.get(s,0))
            reward = self.states_value.get(s,0)


    def reset(self):
        # we reset states but not values, we keep refining those
        self.states = []
        self.board.state = START
          

    # policy is a map of states to values
    def save_policy(self):
        _file = open('policy_grid', 'wb')
        pickle.dump(self.states_value, _file)
        _file.close()

    def read_policy(self):
        _file = open('policy_grid', 'rb')
        self.states_value = pickle.load(_file)
        _file.close()

    def print_state_values(self):
        for i in range(0, 3):
            print('-----------------')
            out = '| '
            for j in range(0,4):         
                out += str(round(self.states_value.get((i,j),0),2)) + ' | '        
            print(out)
        print('-----------------')


def play(n):
    board =Board()
    # the agent has a board
    # not so trivial knowing how to model state
    agent = Agent(board,0.9)
    agent.board.printBoard()

    for i in range(0, n):
       
        if agent.board.isEnd():
            print("End State")
            agent.propagateReward()
            agent.print_state_values()
            agent.reset()
        else:
            # keep on playing
            agent.takeAction()
        
        agent.board.printBoard()
            


if __name__ == "__main__":
    print(" Please enter the number of plays like: > gridworld 5")
    play(int(sys.argv[1]))


