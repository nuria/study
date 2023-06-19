#/usr/local/bin

# given salaries and a max implement a cap such salaries over the cap get converted to the cap


# simple method, there must be something better
def main():
    s = [90,30,100,40,20]
    t = 210
    s.sort()
    #cap 60 
    over = t - sum(s)
    # now find what would be teh salary if everyone made the same money
    avg_cap = t/len(s)
    # there will be some salaries over this amount and some under, 
    # the ones under will give us extra budget to distribute over the larger oners

    extra_budget = 0
    top_earners = 0

    for a in s:
        if a <= avg_cap:
            extra_budget += avg_cap - a
        else:
            top_earners +=1 

    
    cap = avg_cap + extra_budget/top_earners 
       
    print ("the cap is :{0}, extra_budget:{1}, top_earners:{2}".format(cap, extra_budget,top_earners))


def smart():
    s = [90,30,100,40,20]
    t = 210
    s.sort()


if __name__=="__main__":
    main()
