#!/usr/local/bin

def main():
    # intervals [[-4,-1], [0,2], [3,6], [7,9],[11,12],[14,17]] (disjointed)
    # add [1,8]
    # result can be represented as a set of disjoined intervals still
    # intervals are sorted when ingested

    I = [[-4,-1], [0,2], [3,6], [7,9],[11,12],[14,17]]
    to_add = [1,8]

    # the union of two closed intervals is s1_start , s2_end
    # how can we use this here
    # brute force will be seeing if interval overlaps and if so 
    # merge start date

    def overlaps(A,B):
        return (A[0] <= B[1] and A[1]>= B[0]) or (B[0]<=A[1] and B[1] >= A[0])

    result = []

    i = 0
    while i < len(I):
        interval  = I[i]
        if not overlaps(interval, to_add):
            result.append(interval)
            i = i + 1
        else:
            # loop through the overlapping intervals
            start = min(interval[0], to_add[0])
            end = max(interval[1], to_add[1])
            
            while overlaps(interval, to_add) and i < len(I):
                end = max(interval[1], end)
                i = i + 1
                interval = I[i]
            result.append([start, end])

    print result


if __name__=="__main__":
    main()
