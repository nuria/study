#!usr/local/bin/python
# Generate all possible words from telephone numeric key pad
# for an arbitrary length of digits.
# so given  2276696 ACRONYM is a word

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')

distionary = []

def generate(n):
    global dictionary

    # we are returning a list of letters
    if len(n) == 1:
        return list(MAPPING[int(n[0])])
    else:
        possibilities = generate(n[1:])
        current_mapping = list(MAPPING[int(n[0])])

        words = []
        for ch in current_mapping:
            for p in possibilities:

                words.append(ch + p)

        return words

if __name__=="__main__":
    print generate(list('2276696'))



