#!/usr/local/bin


def main():

    A = [310,315,275,295,260,270,290,230,255,250]

    # find the maximun profit that can be made by buying and selling
    # in this case buying at 260, selling at 290, profit is 30

    max_diff = 0

    # o (n2)
    for i in range(0,len(A)):
        for j in range(i+1, len(A)):
            if A[j] - A[i] > max_diff:
                max_diff = A[j]- A[i]


    print (max_diff)

    # now how can you do this in 1 pass
    # keep track of increasing sequence 
    stack = []

    max_diff = 0
    stack.append(A[0])

    for i in range(1, len(A)):
        
        # test whether next number is higher , update max
        if (len(stack) > 0 and A[i] > stack[-1]):
            if A[i]- stack[-1] > max_diff:
                max_diff = A[i] - stack[-1]
        else:
            while len(stack)> 0 and  A[i] < stack[-1]:
                stack.pop()
            stack.append(A[i])
        
        print ("{0}, {1}".format(stack, max_diff))
    
    print(max_diff)



if __name__=="__main__":
    main()
