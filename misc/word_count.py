#!/usr/local/bin
# text of question here: https://medium.com/100-days-of-leetcode/day-13-word-count-engine-dcb2892c17f5
import collections 
import string


_input = "Practice makes perfect. You’ll only get Perfect by practice. just more practice! "

_output=" [ [“practice”, “3”], [“perfect”, “2”],[“makes”, “1”], [“youll”, “1”], [“only”, “1”],[“get”, “1”], [“by”, “1”], [“just”, “1”] , ['more', '1'] ] "

def word_count(_input):
    
    def normalize(w):
        w = w.lower()
        r = ''
        for c in w:
            if c in string.ascii_lowercase:
                r += c
        return r

    # remove punctuation
    # store ocurrences of word on sentence
    # store ocurrences of word
    
    
    c = {}
    original = {}
    

    items = _input.split()
    i = 0
    for w in items:
        w = normalize(w)

        if c.get(w) is None:
            c[w] = 0
            original[w] = i
            i = i +1
        c[w] += 1


    result = []

    for k in c.keys():
        result.append([k, c[k]])

    result.sort(key=lambda x:(c[x[0]], x[1]), reverse=True)

    # TODO include original order
    print(result)
    print(_output)

word_count(_input)


