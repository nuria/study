#!/usr/bin/python

# Find forum nodes where "body" contains only one sentence.
# We define sentence as a "body" that contains either none of the following
# 3 punctuation marks ".!?" , or only one of them as the last character in the body.
# You should not parse the HTML inside body, or pay attention to new lines.

# id"    "title" "tagnames"  "author_id" "body"  "node_type" "parent_id" "abs_parent_id"

import sys
import csv
import re

def is_one_sentence(txt):
    '''
    Return:
        True if this text is consider a one liner, false otherwise.
    '''
    txt = txt.strip()

    # python's regex look like perls but behave differently
    # see http://www.johndcook.com/python_regex.html
    # two pass for simplicity
    m = re.findall(r'\.|!|\?',txt)

    # make sure only one punctuation is returned

    if len(m) == 1:
        # now make sure the match is at the end of the string
        m = re.search(r'(\.|!|\?)\s?$',txt)
        if m is None:
            return False
        else:
            return True
    elif len(m) == 0
        # no punctuation, also considered a 1 liner
        return True
    else:
        return False



# read data as csv
reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    body = line[4]
    if is_one_sentence(body) is True:
        # node-type is item 6
        writer.writerow(line)
