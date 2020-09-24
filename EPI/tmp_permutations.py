# /usr/local/bin


# find all permutations of s within b
def find_perms(s, b):

    import collections

    # o(len(s)) time o(len(s)) space
    c = collections.Counter(s)

    # in order to be a permutation a string needs to have
    # the configuration of 'c'
    # in terms of keys and ocurrences

    # we can walk the other string in groups of 3
    print s
    print b
    len_s = len(s)

    perm = []
    for i in range(0, len(b) -len(s) + 1 ):
        # o (len(s)) space and time
        group = collections.Counter(b[i:i+len_s:])

        # o(len(s) time
        if group == c:
            perm.append(b[i:i+len_s:])

    # complexity is o(len(s)) in space and o(len(s)* len(b)) time
    return perm


if __name__=="__main__":

    print find_perms("abc", "holaquetalabccab")
