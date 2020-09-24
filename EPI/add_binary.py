#!usr/local/bin

def add_binary(n1,n2):

    # assuming inputs are numbers

    result = []


    # get lowest significant bit
    carry = 0
    counter = 0


    while n1 >> counter > 0 or n2 >> counter >0:


        if (n1 >> counter) > 0:
            b1 = n1 >> counter & 1
        else:
            b1 = 0

        if (n2 >> counter) > 0:
            b2 = n2 >> counter & 1
        else:
            b2 = 0


        s = b1 + b2 + carry
        if s < 2:
            result.append(s)
        elif  s == 2:
            carry = 1
            result.append(0)
        else:
            carry =1
            result.append(1)

        counter += 1


    if carry:
        result.append(carry)
    result.reverse()

    return result

if __name__=="__main__":
    print add_binary(7, 7)
