#!/usr/local/bin
"""
Can you justify input text represented by an array of words so it looks pretty when printed and the whitespaces are balanced?
"""
import unittest

EMPTY =' '

k = 11


def right_justify_line(words):

    # k is line length 
    global k  # cause last char is reserved for line break
    total_chars = sum(map(lambda x : len(x), words))
    
    empty_spaces = k - total_chars
    
    if len(words) == 1:
        return words
    
    if empty_spaces == 1:
        return list(words[0]) + [EMPTY] +  list(words[1])
    
    # more than one space
    separation = empty_spaces/(len(words)-1)
    
    line = []
    
    for w in words[:len(words)-1]:
        
        line.append(w)
        for s in range(0,separation):
            line.append(EMPTY)


    if empty_spaces % 2 == 1:
        line.append(EMPTY)
    
    line.append(words[-1])
        
    return line


def left_justify_line(words):
    l = []
    for w in words[0:-1]:
        l.append(w)
        l.append(EMPTY)

    l.append(words[-1])
    return l

class TestSuite(unittest.TestCase):
    def test_happy_case(self):
        words =['aa', 'bb', 'cc']
        self.assertEqual(right_justify_line(words), ['aa',EMPTY,EMPTY, 'bb',EMPTY, EMPTY, EMPTY,'cc'])
    
    def test_last_line_left(selft):
        words =['aa', 'bb']
        selft.assertEqual(left_justify_line(words), ['aa', EMPTY, 'bb'])

    def test_two_words(self):
        words= ['a', 'b']
        E = EMPTY
        self.assertEqual(right_justify_line(words), ['a',E,E,E,E,E,E,E,E,E,E,'b'])

def main():
    words = ['algodaily','is','awesome','and','you','can','text','justify','all','types','of','text','and','words' ]

    global k 

    result = \
    'algodaily  \n' + \
    'is  awesome\n' +\
    'and you can\n' +\
    'text       \n' +\
    'justify all\n' +\
    'types    of\n' +\
    'text    and\n' +\
    'words      ';


    #print result

    paper= [ [EMPTY] * k  for i in range(0, len(words) + 1) ]

    # if there is only one word we cannot right justify
    # keep track of num_words per line


    w = 0 
    l = 0
    num_words_line =[]
    chars_in_line = 0
    
    while  w < len(words):
        word = words[w]
        # all words need to be less than length of line
        
        min_separating = max(1,len(num_words_line)-1)

        if chars_in_line + min_separating + len(word) < k + 1:
            # increment word
            w = w + 1 
            num_words_line.append(word)
            chars_in_line += len(word)
        else:
            # cannot insert
            # move line index
            line = right_justify_line(num_words_line)
            paper[l] = line 
            # increment line i and try again
            l = l + 1
            num_words_line =[] 
            chars_in_line = 0
    
    paper[l] = left_justify_line(num_words_line)
    
    paper = paper[0:l+1]
    
    for line in paper:
        txt =''
        for c in line:
            txt += c
        txt += "\n"
        print txt

    for l in paper:
        print l
    



if __name__=="__main__":
    main()
    unittest.main().result
