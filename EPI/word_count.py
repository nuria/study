#usr/local/bin/python
# coding: utf-8
"""
input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"],
          ["get", "1"], ["by", "1"], ["just", "1"] ]

Resolve ties adding to result 1st the word that appaears on teh original first

"""
import collections
import re

def word_count(s):

    # split by words, remove not whitespace
    result = []
    s = re.sub('\W', ' ',s.lower())
    words = s.split()

    c = collections.Counter(words)
    d = {}

    index = 0
    for item in words:
        d[item] = index
        index+= 1
    # now we need to order said ocurrences

    for k in c.keys():
        result.append([k,c[k]])


    # now we have a list that we need to sort

    def custom_sort(a,b):

        if a[1] > b[1]:
            return -1
        elif b[1] > a[1]:
            return 1
        else:
            # equal
            ka = a[0]
            kb = b[0]
            if d[ka] > d[kb]:
                return -1
            else:
                return  1


    result.sort(custom_sort)

    return result

if __name__=="__main__":

    s = "Practice·makes·perfect.·you'll·only get·Perfect·by·practice.·just·practice!"
    print word_count(s)

