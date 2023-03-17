#!/usr/local/bin

def main():
    # award budget cuts

    
    def find_cap(grants, budget):
        grants.sort()
        running_budget = 0


        i = 0
        # [2,50, 100, 120, 1000]
        # budget = 2 plus estimation is 2*rest
        # next budget is 2+5 + %*rest
        i = 0
        while running_budget < budget:
            running_budget = sum(grants[0:i]) + grants[i] * (len(grants) -i)
            i = i + 1

        # item that breaks the budget
        i = i -1

        excess = budget - running_budget
        #2+50 =52 + 50 *3 = 202
        # 190 -202 = 12 
        # cap will be 50 if it wasn't for the extra 12
        #(50-x) * 4 < 190
        # 190/4 -50
        to_remove = (-1)*( budget/(len(grants)-i) - grants[i])
        
        
        return  grants[i] - to_remove


    # make grants firt on budget affecting the least ammount of grants possible
    # possible by applying a cap on all grants, return the cap
    grants = [2, 100, 50, 120, 1000]
    budget = 190

    # output is 47
    print find_cap(grants, budget)

if __name__=="__main__":
    main()
