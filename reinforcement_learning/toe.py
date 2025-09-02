#!/opt/nflx/python
import unittest
import copy
import pickle
import numpy as np

"""
tik tak toe example 
from http://incompleteideas.net/book/RLbook2020.pdf , page 30
Use code from : https://medium.com/data-science/reinforcement-learning-implement-tictactoe-189582bea542
changing some things arround

Approach to tik tak toe problem using a value function 
that maximizes rewards over the long term

First we would set up a table of numbers, one for each possible state
of the game. 
Each number will be the latest estimate of the probability of our winning
from that state. 
We treat this estimate as the state’s value, and the whole table is the
learned value function. 

State A has higher value than state B, or is considered “better”
than state B, if the current estimate of the probability of our winning from A is higher
than it is from B

States with three XXX have probability of P(winning) =1
XX =>P(winning) =0.5, OOO p(winning) =0

We then play many games against the opponent.and select states greedily ,
those that,on our table, have the higest proability of winning
"""

X = 'X'

O = '0'

EMPTY = '.'

EMPTY_STATE = [[EMPTY,EMPTY,EMPTY] for i in range(0,3)]


# three rows or diagonals that are the same
"""
We compute winner for X player
returns True if 'X' player won
returns false if 'O' player won
if None no win
"""
def is_winner(matrix):
    winner = None

    # are any rows all 0 or X
    for i in range(0, 3):
        if np.array_equal(matrix[i], [X,X,X]):
            winner = True
        elif  np.array_equal(matrix[i], [O,O,O]):
            winner = False

   # are there columns
    for i in range(0,3):
        if matrix[0,i] == matrix[1,i] and matrix[0,i] == matrix[2,i]  and matrix[0,i] != EMPTY:
            if matrix[0,i] == X:
                winner = True
            else:
                winner = False

    # are there diagonals
    if matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2] and matrix[0][0] != EMPTY:
        if matrix[0][0] == X:
            winner = True
        else:
            winner = False

    if matrix[0][2] == matrix[1][1] and matrix[0][2] == matrix[2][0] and matrix[0][2] != EMPTY:
        if matrix[0][2] == X:
            winner = True
        else:
            winner = False


    return winner

class State:
    def __init__(self, p1, p2):
        self.matrix = np.array([[EMPTY,EMPTY,EMPTY], [EMPTY,EMPTY,EMPTY], [EMPTY,EMPTY,EMPTY]])
        self.p1 = p1
        self.p2 = p2

        # current player, p1 plays 1st
        self.current_player = p1
        self.is_end = False

    """
    deterministic hash 
    from matrix state
    """
    def get_hash(self):
     
        hash_val = ''
        for i in range(0,3):
            hash_val+="".join(self.matrix[i])
        return hash_val


    """
    returns array with empty positions
    """
    def available_positions(self):
        positions = []
        for i in range(0,3):
            for j in range(0,3):
                if self.matrix[i][j] == EMPTY:
                    positions.append((i,j))
        if len(positions) == 0:
            self.is_end = True
        return positions

    """
    put piece on position i, j
    board keeps a reference to the player playing
    """
    def next_state(self, position):
    
        if self.matrix[position] == EMPTY:
            #print("setting piece on position {0}".format(position))
            self.matrix[position] = self.current_player.piece
        else:
            print("error! position {0} is occupied by {1}".format(position, self.matrix[position]))
            print(self.matrix)
            exit(1)     
        
        # switch player
        if self.current_player == self.p1:
            self.current_player = self.p2
        else:
            self.current_player = self.p1
    
        ####### move to play #####
        # we are playing with 'X'
        # winner false means 'O' won
        # otherwise winner is undefined
        winner = is_winner(self.matrix)

        if winner is None:
            if len(self.available_positions()) != 0:
                # continue playing
                self.is_end = False
        else:
            # winner is defined
            self.is_end = True

        
    # only when game ends
    def give_reward(self):
        print(self.matrix)
        
        result = is_winner(self.matrix)
        if result is True:
            # reward for p1 , X
            print("X wins")
            self.p1.feed_reward(1)
            self.p2.feed_reward(0)
        elif result is False:
            # reward for p2
            print("O wins")
            self.p1.feed_reward(0)
            self.p2.feed_reward(1)
        else:
            print("Not a winner")
            # not a winner
            # but no available positions
            self.p1.feed_reward(0.5)
            self.p2.feed_reward(0.5)
    

"""
Player class memoizes all positions taken  
"""
class Player:
    def __init__(self, piece, exp_rate=0.3):
        self.piece = piece
        self.states = [] # record all positions taken
        self.states_value = {}
        self.decay = 0.9
        # balance greedy choices (exploit) with random choice (explore)
        self.exp_rate = exp_rate

    """
    At the end of the game 
    backpropagate the reward
    """
    def feed_reward(self, reward):
        for st in reversed (self.states):
            if self.states_value.get(st) is None:
                self.states_value[st] = 0
            # the reward is biggest on last state (the winning one)
            self.states_value[st] +=  reward * self.decay  -  self.states_value[st]
            reward = self.states_value[st]


    def reset(self):
        self.states = []


    def choose_action(self, state): 

        # first decide if explore of exploit 
        import random
        positions = state.available_positions()
       
        _max = float('-inf')
        next_position = None

        if random.random() < 0.3:
            # explore, of available positions choose one
            next_position = positions[random.randint(0, len(positions)-1)]
            print("exploring")
        else:
            print("exploiting")
            # exploit
            # choose state with max_value?
            # of the possible future choices
            for p in positions:
               
                board_copy = copy.deepcopy(state)
                 
                board_copy.next_state(p)
                hash_value = board_copy.get_hash()

                  
                if self.states_value.get(hash_value, 0) > _max:
                    next_position = p
                    _max = self.states_value.get(hash_value,0)

      
        return next_position
    
    def save_policy(self):
        fw = open('policy_' + str(self.piece), 'wb')
        pickle.dump(self.states_value, fw)
        fw.close()

    def read_policy(self):
        fr = open('policy_' + str(self.piece), 'rb')
        self.states_value = pickle.load(fr)
        fr.close()

class HumanPlayer:
    def __init__(self, piece):
        self.piece = piece

    def choose_action(self, positions):
        while True:
            row = int(input("Input your action row:"))
            col = int(input("Input your action col:"))
            action = (row, col)
            if action in positions:
                return action

    # append a hash state
    def add_state(self, state):
        pass

    # at the end of game, backpropagate and update states value
    def feed_reward(self, reward):
        pass

    def reset(self):
        pass




def play(n):
    # set up the game
    p1 = Player("X")
    p2 = Player("O")

    for i in range(0,n):
        print("Game ", i+1)
        # save policy everytime
        p1.save_policy()
        p2.save_policy()
        p1.reset()
        p2.reset()
        board = State(p1,p2)
        while not board.is_end:
            # player p1 goes 1st
            next_position = p1.choose_action(board)
            # next_state sets end if pertains
            board.next_state(next_position)
            if board.is_end:
                # end game
                # give reward and break
                board.give_reward()     
                break

            # not end of game, next play
            else:
                # player p2 goes next
                next_position = p2.choose_action(board)
                # next_state sets end if pertains
                board.next_state(next_position)
                if board.is_end:
                    # end game
                    # give reward and break
                    board.give_reward()
                    break

         
            
def play_with_human():
     # set up the game
    p1 = Player("X")
    p1.read_policy()
    p2 = HumanPlayer("O")

    print("Game on")

  
    board = State(p1,p2)
    while not board.is_end:
     
        # player p1 goes 1st
        next_position = p1.choose_action(board)
        # next_state sets end if pertains
        board.next_state(next_position)
        print(board.matrix)
        if board.is_end:
            # end game
            # give reward and break
            board.give_reward()     
            break

        # not end of game, next play
        else:
            # player p2 goes next
            next_position = p2.choose_action(board.available_positions())
            # next_state sets end if pertains
            board.next_state(next_position)
            if board.is_end:
                # end game
                # give reward and break
                board.give_reward()
                break


class TestSuite(unittest.TestCase):
    
    def test_happy_case_win(self):
        p1 = Player("X")
        p2 = Player("O")
        state = State(p1,p2)
        print(state.matrix)
        assert(is_winner(state.matrix) is not True)

    def test_hash_val_happy_case(self):
        p1 = Player("X")
        p2 = Player("O")
        state = State(p1,p2)
        new_state = copy.deepcopy(state)
        assert(state.get_hash()== new_state.get_hash())

    def test_hash_val_move(self):
        p1 = Player("X")
        p2 = Player("O")
        board = State(p1,p2)
        next_position = p1.choose_action(board)
        pre_hash = board.get_hash()
        # next_state sets end if pertains
        board.next_state(next_position)
        assert(pre_hash != board.get_hash())

    def test_wins(self):
        p1 = Player("X")
        p2 = Player("O")
        state = State(p1,p2)
        state.next_state((0, 0))  # X
        state.next_state((1, 1))  # O
        state.next_state((0, 1))  # X
        state.next_state((1, 0))  # O
        state.next_state((0, 2))  # X wins
        
        assert(is_winner(state.matrix) is True)

    def test_no_wins(self):
        p1 = Player("X")
        p2 = Player("O")
        state = State(p1,p2)
        state.next_state((0, 0))  # X
        state.next_state((1, 1))  # O
        state.next_state((0, 1))  # X
        state.next_state((1, 0))  # O
        # nobody wins
        print(state.matrix)
        print("is winner {0}".format(is_winner(state.matrix)))
        
        assert(is_winner(state.matrix) is None)
        

if __name__ =="__main__":
    #unittest.main().run
    # we need to run play to create policy
    # to use agains a human oponent
    # play(1000)
    # this would use the policy created
    play_with_human()




