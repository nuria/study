#!/usr/local/bin
import sys 

#L < R R > R
class BSTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left

    def __repr__(self):
        t = "{"

        if self.left is not None:
            t += "L" + str(self.left)

        t +=" " + str(self.value)+ " "

        if self.right is not None:
            t += "R" + str(self.right) 
        
        t +=   "}"
        return t

 
# is this a recursive algorithm that finds middle of array and assigns left and right
# that way height is as small as possible
# taht is a possible solution but it might not be the most optimal 

def  main():
    # sorted array of frequencies, build BST that minimizes height of tree
    A = eval(sys.argv[1])
    
    # have in mind that array is sorted
    def bst_from_list(A):

        if len(A) == 1:
            return BSTNode(A[0])
        elif len(A)==2:
            left = BSTNode(A[1])
            return BSTNode(A[0], left)

        m = int(len(A)/2)
        
        left = bst_from_list(A[0:m])
        right = bst_from_list(A[m+1:])
        root = BSTNode(A[m], left, right)

        return root

    root = bst_from_list(A)

    print (root)


def optimal_bst_dp():
    
    A = eval(sys.argv[1])

    # we can also find all possible solutions of tree 
    # using the metric of search cost as a measure of how efficient is the tree
    # https://www.techiedelight.com/find-optimal-cost-to-construct-binary-search-tree/
    # this is a particular DP problem cause we care about both parts of solution
    A = eval(sys.argv[1])

    n = len(A)
    

    DP = [ [0] * (n+1)  for i in range(0, n+1)]
    # initialize the DP matrix
    # DP[i][j] = cost of searching tree containing i to j nodes
    # DP[i][i] = one node
    # DP[0][i] = one node as well ?
    
    # single key
    for i in range(0, n):
        DP[i][i] = A[i]

    # DP[i][j] = cost of tree that has nodes from i to j
    # DP[i][j]= A[r] + A[1,r-1] +A[r+1,j], solution is DP[0][N]
    # also here we care about the parts of solution where j> i
    # everything else is zero
    
    # all sizes of sequences (zero index)
    for size in range(1, n + 1):
        # all starting points of sequences
        for i in range(0, n-size+2):
            
            # end of sequence of length size

            j = min(i + size -1, n-1)
            
            cost_i_j = float('inf')

            # consider each key as root and calculate the optimal cost
            base_cost = 0
            for k in range(i, j+1):
                base_cost += A[k] 


            for r in range(i, j+1):
                c = 0
                # cost when A[r] becomes root of this tree
                # cost left subtree
                if r != i:
                    c = c + DP[i][r-1] 
                # cost right subtree
                if r != j:
                    c = c + DP[r+1][j] 
                
                c = c + base_cost
                cost_i_j = min(c, cost_i_j)

            DP[i][j] = cost_i_j

    print (DP)
    print( DP[0][n-1])







if __name__=="__main__":
    main()
    optimal_bst_dp()
