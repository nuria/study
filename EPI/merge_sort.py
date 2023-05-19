#!/usr/local/bin

# merge sort

import sys

def main():
    A = eval(sys.argv[1])

    # split array in two and sort either one

    def sort(A):
        if len(A) ==1:
            return A
        elif len(A) == 2:
            return [min(A), max(A)]
        else:
            m = len(A)/2
            left = sort(A[0:m])
            right = sort(A[m:])

            # put these together
            result = []

            r = 0
            l = 0
            while r <len(right) and l <len(left):
                if left[l] < right[r]:
                    result.append(left[l])
                    l = l + 1
                else:
                    result.append(right[r])
                    r = r + 1
                
            if r < len(right):
                result = result + right[r:]
            if l <len(left):
                result = result +left[l:]

            return result

    print sort(A)   

if __name__=="__main__":
    main()
