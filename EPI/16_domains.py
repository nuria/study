#!usr/local/bin/python



def split(domain, D):
    words = []

    N = len(domain)

    # indexes of matrix denote the possible prtefixes
    # W[0][n] denotes the full word
    # W[n][n] is prefix of teh last character
    # we do not really need the matrix, it is just a means to move
    # through the computations

    # so at any position is not the position before but rather we are looking to see if we find words
    # you can record the length of the last dictionary word, overall?
    last_word = [-1] * len(domain)
    for i in range(0,N):

        for j in  range(i+1,N):
            p = domain[i:j+1]
            print last_word;
            if p in D:
                last_word[j] = j + 1
                words.append(p)

    return (words, last_word)



if __name__=="__main__":
    D = set(['bed', 'bath', 'and', 'beyond', 'hand', 'bat'])
    print split('bedbathandbeyond',D)


