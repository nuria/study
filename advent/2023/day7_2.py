#!/usr/local/bin

import sys
import collections
import functools 
import unittest

ORDER = {'A':10,'K':9,'Q':8,'T':6,'9':5,'8':4,'7':3,'6':2,'5':1,'4':0,'3':-1,'2':-2, 'J':-3}



HANDS = {'five':10,'four':9, 'full_house':8, 'three_of':7, 'two_pair':6, 'one_pair':5, 'high_card':4 }



# returns the classification of hand
def classify(hand):
    h = collections.Counter(hand)
    
    if len(h.keys()) == 1:
        # 5 of a kind
        return 'five'
    
    if len(h.keys())== 2:
        if 4 in h.values():
            # this is a (4, 1) hand
            return 'four'
        else:
            # this is a 3,2 hand
            return 'full_house'

    if len(h.keys()) == 3:
        if 3 in h.values():
            # (3,1,1)
            return 'three_of'
        else:
            # (2,2,1)
            return 'two_pair'
    
    if len(h.keys()) == 4:
        #(2,1,1,1)
        return 'one_pair'
    
    if len(h.keys()) == 5:
        # all distinct
        return 'high_card'
        


def classify_wJ(hand):
    h = collections.Counter(hand)
    _type = classify(hand)
    
    # now count number of 'Js'
    j = h['J']
    # how do we escalate the hand
    # starting at the top
    
    if _type =='four':
        #(X,X,X,X,J)
        return 'five'

    if _type =='full_house':
        # (X,X,X, J, J)
        return 'five'

    if _type =='three_of':
        # (X, X, X, J, Y) => (X,X,X,X,Y)
        # (J,J,J, X,Y) => (X,X,X,X,Y)
        return 'four'

    if _type == 'two_pair':
        # (X,X,J,J,Y) or (X,X,Y, Y, J)
        if j == 2:
            return 'four'
        else: # j=1
            return 'full_house'

    if _type =='one_pair':
        # (X,X,Y,Z,J) => (X,X,X,Y,Z)
        # (J,J, X, Y, Z) => (X,X,X,Y,Z)    
        return 'three_of'
         
    
    if _type=='high_card':
        # (X, Y,Z, J,N) => (X,Y,Z,J,J)
        return 'one_pair'

    print("j type, not touched: {0}".format(hand))
    return _type




# custom function to sort
# does this needs to be implemented in some fancy way?
# if item1 > item 2 retuns 1
# if item1 < item 2 returns -1
# else 0
def compare_hands(hand1, hand2):
    
    h1 = hand1[0]
    h2 = hand2[0]

    # clunky but whatevah
    if 'J' in h1:
        type1 = classify_wJ(h1)
    else:
        type1 = classify(h1)
    if 'J' in h2:
        type2 = classify_wJ(h2)
    else:
        type2 = classify(h2)


    if HANDS[type1] > HANDS[type2]:
        return 1
    elif HANDS[type1] < HANDS[type2]:
        return -1

    # equal, proceed

    # move onto individual cards
    i = 0

    h1 = hand1[0]
    h2 = hand2[0]

    while (i < len(h1)):
        cmp = compare_cards(h1[i], h2[i])
        if cmp!= 0:
            return cmp
        i = i + 1
    
    print ("tied")
    # looks like none of them are tied?
    return 0


# absolute ordering
def compare_cards( char1, char2):
    if ORDER[char1] > ORDER[char2]:
        return 1
    elif ORDER[char1] < ORDER[char2]:
        return -1
    else:
        return 0



def main():

    f = open(sys.argv[1])

    hands = []

    root = None

    for l in f:
        (h, b) = (l.strip()).split()
        hands.append((h, b))

    print(hands)
    print ("********")
    # call sorting function on hands
    
    wrapper = functools.cmp_to_key(compare_hands)

    hands.sort(key=wrapper)# reverse=True)
    print(hands)


    # compute rank, but some must be tied
    result = 0

    for i  in range(0,len(hands)):
        
        bet= hands[i][1]
        result += (i+1) * int(bet)

    print(result)


class TestCase(unittest.TestCase):
    def test_happy_case(self):
        c1 = ("33332",1)
        c2 =("2AAAA",2)
        result = compare_hands(c1, c2)
        self.assertTrue(result==1)
        c1 = ("77888","")
        c2 = ("77788", "")
        self.assertTrue(compare_hands(c1,c2)==1)

        
    def test_classify(self):
        self.assertTrue(classify("33332")=="four")
        self.assertTrue(classify("23456")=="high_card")
        self.assertTrue(classify("AA8AA")=="four")

    def test_j(self):
        self.assertTrue(classify_wJ("QJJQ2")=="four")
        c1 = classify_wJ("JKKK2")
        c2 = classify("QQQQ2")
        self.assertTrue(c1==c2)
        self.assertTrue(compare_hands(("JKKK2",), ("QQQQ2",)) < 0 )

        self.assertTrue(classify_wJ("T55J5")=="four")
        self.assertTrue(classify_wJ("T55J5")=="four")
        self.assertTrue(classify_wJ("KTJJT")=="four")

if __name__=="__main__":
    main()
    #unittest.main().result
