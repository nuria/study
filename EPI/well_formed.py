#!usr/local/bin

def is_well_formed(s):
    # need to make sure every parenthesis has its counter type
    # will store entries per "char"

    d = {}

    d["}"] = 0
    d[")"] = 0
    d["]"] = 0


    # notion of  a partner

    while len(s) >0:
        # deque item
        item = s[len(s)-1]
        if item in d.keys():
            d[item] += 1
        else:
            if item == "{":
                d["}"] -= 1
            elif item =="(":
                d[")"] -= 1
            elif item =="[":
                d["]"] -= 1
        s = s[0:len(s)-1]
    # all keys shoudl eb zero
    well_formed = True

    for k in d.keys():
        if d[k] != 0:
            return False

    return well_formed

# needs to keep a notion of order
def is_well_formed2(s):
    left_chars = []
    lookup = {'(':')','{':'}', '[':']'}
    for c in s:
        print c
        if c in lookup:
            left_chars.append(c)
            print left_chars
        elif not left_chars or lookup[left_chars.pop()] != c:
            return False

    return not left_chars


if __name__ =="__main__":
    print is_well_formed2("([]){}")
    #print is_well_formed2("{)")
    # wrong code, matches the last one
    #print is_well_formed2("(()][){}")

