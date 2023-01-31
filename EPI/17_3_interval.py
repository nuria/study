#/usr/bin
import sys

# you are given a set of closed intervals
# design an efficient algorithm for finding 
# a minimum size interval that has a point in all the intervals

# t = (s,e)
# c =int
def contained(t,c):
    if t[0] <=c and c<= t[1]:
        return True
    else:
        return False



def find_interval(l):
    # initialize min and max
    # sort list of right endpoint 

    l.sort(key=lambda x:x[1])
    print l

    #end of 1st interval, soonest stop
    S = l[0][1]
    E = S
    for task in l:
        # loop through the ones this cover until we find the one we do not 
        if not contained(task, S) and not contained(task,E):
            # this interval is not covered we pick it as the end
            E = task[0]
        



    return (S, E)

def main():
    
    l = eval(sys.argv[1])
    print l 
    
    # interval that has a point in each
    print find_interval(l)    



if __name__=="__main__":
    main()
