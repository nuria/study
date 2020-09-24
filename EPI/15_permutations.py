#!usr/local/bin

result = []

def perm(l):
    if len(l) == 1:
        return [l]

    result =[]
    for item in l:
        tmp = l[:]
        # o(n)
        tmp.remove(item)
        right = perm(tmp)

        for r in right:
            result.append([item] + r)

    return result






if __name__ == "__main__":
    print perm([2,3,5,7])
