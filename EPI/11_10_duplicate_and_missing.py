#/usr/local/bin

def main():
    # how to xor a bunch of numbers
    l = [1,2,3,4,4,5,6,7] #0 is missing, 4 is duplicated, find both at thesame time
    N = 8
    # if the sries from 0..n is complete xor is zero
    # if a number is missing xor is that number

    xor_series  = l[0]
    
    for e in l[1:]:
        xor_series = xor_series ^ e
    
    print "xor_series: {0}".format(xor_series)

    # all bits are set to 0 except the least significant one
    differ_bit = xor_series & ~(xor_series-1)

    print "differ bit:{0}".format(differ_bit)

    candidate  = 0

    for e in l:
        if e & differ_bit: # not zero
            candidate = candidate ^ e 
            # now look in array


    if candidate in l:
        print "duplicate is :{0}".format(candidate)
    else:
        print "missing value is :{0}".format(candidate)



if __name__=="__main__":
    main()
