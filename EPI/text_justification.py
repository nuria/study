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
        return list(words[0]) + [EMPTY] * (k-len(words[0]))
    
    if empty_spaces == 1:
        return list(words[0]) + [EMPTY] +  list(words[1])
    
    if len(words) == 2:
        line = list(words[0]) + [EMPTY] * empty_spaces + list(words[1])
        return line
    # more than two words
    separation = empty_spaces/(len(words)-1)
    
    line = []
    
    for w in words[:len(words)-1]:
        line+= list(w) + [EMPTY] * separation

    if empty_spaces % 2 == 1:
        line+= [EMPTY]
    
    line += list(words[-1])
        
    return line



    



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
    
    num_words = {}


    w = 0 
    l = 0
    
    while  w < len(words):
        word = words[w]
        # all words need to be less than length of line
        can_insert = False
        
        if num_words.get(l) is None:
            can_insert = True
            num_words[l] = []
        else:
            chars_in_line = sum(map(lambda x:len(x), num_words[l]))
            min_separating = max(1,len(num_words[l])-1)

            if chars_in_line + min_separating + len(word) < k + 1:
                can_insert = True

        if can_insert:
            # increment word
            w = w + 1 
            num_words[l].append(word)
        else:
            # cannot insert
            # move line index
            line = right_justify_line(num_words[l])
            paper[l] = line 
            # increment line i and try again
            l = l + 1
        
    
    paper[l] = right_justify_line(num_words[l])
    
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
    #unittest.main().result
