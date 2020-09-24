#usr/local/bin/python

def decrypt(word):
    ASCII_START = 97
    # step 1  covert letters to ascii values
    def step1(word):
        r = []
        for w in word:
            r.append(ord(w))
        print r
        return r
    # step 2
    # substract the value of prior letter , if not in range add 26
    # as many times as needed
    # if first letter, substract 1
    def step2(numbers):
        value_to_substract = 1
        r = []
        for i in range(0,len(numbers)):
            if i > 0:
                value_to_substract = numbers[i-1]
            tmp = numbers[i] - value_to_substract
            while(tmp < ASCII_START ):
                tmp += 26

            r.append(tmp)

        print r
        return r

    def step3(numbers):
        r = []
        for n in numbers:
            r.append(chr(n))
        return r

    return step3(step2(step1(word)))




if __name__=="__main__":
    # should return 'crime'
    print decrypt('dnotq')
