#!/usr/local/bin/
import unittest

"""
Sort of edit distance among two strings without DP
# write char if char does not need to be edited 
  
  # or write "-C" if not included
  # or write +C if an addition is needed
  
  # result is the sequence 
  if there are multiple answers use the one that favors removing from source first
  

"""

def min_edits(source, target):

    def edits(source, target, s):
       
        #print("source:{0}, target :{1}, solutions:{2}".format(source, target, s))

        if len(source) == 0 and len(target) == 0:
            return s

        elif len(source) == 0 or len(target)== 0:
            t = None
            if len(source) == 0 :
                t = map(lambda x: "+"+x, target)
               
            elif len(target) == 0:
                # remove all letters from target
                t = map(lambda x: "-"+x, source)

            for i in range(len(s)):
                s[i] = s[i] + list(t)
            return s


        if source[0] == target[0]:
            for i in range(len(s)):
                s[i].append(source[0])

            return edits(source[1:], target[1:], s[:])

        # case the 1st char is different
        # remove it and compare rest of source to target
        solutions_a = s[:]

        for i in range(len(s)):
            s[i].append("-"+source[0])

        solutions_1 = edits(source[1:], target, solutions_a)

        # which is length of solutions 1
        _max = None
        
        min_len = min(list(map(lambda x: len(x) , solutions_1)))

        solutions_b = s[:]

        # add it and compare new addition
        
        for i in range(len(s)):
            s[i].append("+"+target[0])

        solutions_2 = edits(source, target[1:], solutions_b)
        
        for s in solutions_2:
            if len(s) <min_len:
                solutions_1.append(s)
        

        return solutions_1
            

    return edits(source, target, [[]])
    




class TestCase(unittest.TestCase):
    def test_hayy_case(self):
        source = "ABCDEFG"
        target ="ABDFFGH"
       
        output = ["A","B","-C","D","-E","F","+F","G","+H"]
    
        self.assertEqual(min_edits(source, target), output)

    def test_hayy_case2(self):
        source = "ABC"
        target ="ABDFFGH"
        print('solutions')
        print(min_edits(source, target))


if __name__=="__main__":
    unittest.main().result
