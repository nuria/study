#!/usr/local/bin

"""
You have traffic at various timestamps and a window length 
compute  for each input timestamp the maximun traffic over the window length

"""
#(ts,traffic)


def main():
    _input =[(0, 1.3), (2, 2.25), (3,3.7), (5, 1.4), (6, 2.6), (8, 2.2), (9, 1.7), (14, 1.1)]
    w = 3
    # identify max within windown length
    # seems like we just need the second item?


    # ws: window start, w : window size
    # given a window returns the index of the maximun entry
    def find_max(A, ws, w):
        i = 0 
        _max = 0
        for k in range(ws, ws+w):
            if A[k] >_max:
                i = k
                _max = A[k]

        return i

    A = map(lambda x:x[1],_input)

    print A
    result = []
    i = 0

    # fill in the values until we get to our window size
    while i < w-1:
        result.append(A[i])
        i = i + 1

    ws = 0
    local_max_index = find_max(_input, ws, w)
    
    result.append(A[local_max_index])

    while ws < len(A)-w:
        
        # given a window returns the index of the maximun entry
        ws = ws + 1

        if local_max_index < ws + w and local_max_index >= ws:
            # do not change max
            result.append(A[local_max_index])
        else:
            local_max_index = find_max(A,ws,w)
            result.append(A[local_max_index])
            
        print "window: {0}, max: {1} ".format(A[ws:ws+w], A[local_max_index])

    print result



if __name__=="__main__":
    main()
