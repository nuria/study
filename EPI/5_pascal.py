#!usr/local/bin


def generate_pascal_triangle(n):
    # modeling like a matrix
    # n is the number of levels
    p = []
    p.append([])
    for i in range(1, n+1):
        print p
        if i == 1:
            p.append([1])
        elif i == 2:
            p.append([1,1])
        else:
            #  the first and last elements are 1s
            l = [1]
            # now look at the "row"prior
            # careful, 0 index
            prior_row = p[i-1]
            for k in range(0, i-2):
                value = prior_row[k+1] + prior_row[k]
                l.append(value)
            l.append(1)
            p.append(l)

    return p


if __name__=="__main__":
    print generate_pascal_triangle(6)
