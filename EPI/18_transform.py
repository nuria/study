#!usr/local/bin


import collections

def transform(D, s, t):
    # D is a dictionary of words

    d = collections.deque()

    d.append(s)

    sequence  = []
    sequence.append(s)

    while len(q) >0:
        word = q.popleft()
        sequence.append(word)
        if word == t:
            return sequence

        for i in range(0, len(word)):
            for l in string.ascii_lowercase:
                new_word = word[:i] + c word[i+1:c]
                if new_word in D:
                    q.append(new_word)

        return  -1




if __name__== "__main__":

