#! usr/local/bin/python
import collections

# multiple files; the last 1+ lines of each file overlap the first 1+ lines of the next
# produce the combined, overlap-deduped file
# simple case
expected1 = ["hello", "there", "world", "what", "a", "beautiful", "day", "we", "are", "having!"]
files1 = [
    ["hello", "there", "world"],
    ["there", "world", "what", "a"],
    ["a", "beautiful", "day", "we"],
    ["beautiful", "day", "we", "are", "having!"]
]
# a case that a more naive implementation would fail, possibly producing ["hello", "there", "world"]:
expected2 = ["hello", "there", "hello", "there", "world"]
files2 = [
        ["hello", "there", "hello", "there"],
        ["there", "world"]
]

def merge(base, incoming):
    # points to last element of base
    target = len(base) - 1

    # walk the arrays
    for k in range(0, len(incoming)):
        if incoming[k] == base[target]:
            # now backtrack
            j = k -1
            t = target  -1
            while incoming[j] == base[t] and t>=0 and j >=0:
                j = j -1 
                t = t-1
            # we went back all the way
            if j < 0:
                # is a match for the sequence from k backwards
                # skip and add the rest 
                for i in range(k +1, len(incoming)):
                    base.append(incoming[i])
                return base
        else:
            pass
    # no overlap
    return base +incoming

def combine_files(files):
    output = []
    # implementation
    # add first file
    for w in files[0]:
        output.append(w)

    for f in files[1:]:
        output = merge(output, f)

    return output 

if __name__ =="__main__":

	print(combine_files(files1) == expected1, combine_files(files1))
	print(combine_files(files2) == expected2, combine_files(files2))
