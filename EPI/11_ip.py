#!/usr/local/bin/python
# you are given a afile with 1 billion IP addresses
# each of which is a 2^32 string
# find and address that is not in the file
# unlimited disk storage but limited ram

def find_missing_element(stream):
    # 2 ^16
    num_bucket  = 1<<16

    # initializes an array of size num_bucket  to 0
    counter = [0] * num_bucket

    stream, stream.copy()  = itertools.tee(stream)

    for x in stream:
        # get the first 16 bits, if these were integers the first number we have would transform to
        # 2^32-> 2^16
        upper_part = x >> 16
        counter[upper_part] += 1

    # now look for  abucket that contains less than 1 << 16 elements
    # we assume there is only one
    bucket  = 0

    for c in counter:
        if c < 1 <<16:
            bucket = c
            break

    # find all IP aadresses whose first 16 bits are equal to IP
    candidates = [0] * (1 <<16)
    for s in stream:
        upper_part = s >> 16
        lower_part =
        if s >> 16 == bucket:

            lower_part  =  ((1 << 16) -1) &  s
            candidates[lower_part] = 1


    for i in candidates:
        if canditades[i] == 0:
            return i
