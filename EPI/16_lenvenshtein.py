#!usr/local/bin

# great tutorial at : https://www.geeksforgeeks.org/edit-distance-dp-5/

def lev(str1, str2):
    # if str1[-1] = str2[-1] => move back
    #  if chars are different consider the three cases
    # insertion  str1, str2[len-]
    # deletion str1[len-1], str2[len-1]
    # deletion str1 and str2[len-1]

    # if strings are empty the distance will be the other string

    if len(str1) ==0:
        return len(str2)
    if len(str2) ==0:
        return len(str1)

    # then if not empty

    if str1[-1] == str2[-1]:
        return lev(str1[0:len(str1)-1], str2[0:len(str2) -1])
    else:
        l1 = lev(str1[0:len(str1)-1], str2)
        l2 = lev(str1, str2[0:len(str2) -1])
        l3 = lev(str1[0:len(str1)-1],str2)

        return 1 + min(l1,l2,l3)



if __name__=="__main__":
    print lev("saturday", "sunday")

