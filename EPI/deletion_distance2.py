#!/usr/local/bin
import unittest

def deletion_distance(str1, str2):
  
    def deletion(s1, s2):
    
        if len(s1) == 0:
            return len(s2) 
        
        elif len(s2) == 0:
            return len(s1) 
        
        # now let's look at 1st char
        c1 = s1[0]
        c2 = s2[0]
        
        print("{0}, {1}".format(s1,s2))
        
        if c1 == c2:
          
            return  deletion(s1[1:], s2[1:])
        else:
            print("{0}, {1}".format(s1,s2))
            
            d1 = deletion(s1, s2[1:] )
            d2 = deletion(s1[1:], s2)
          
            print ("{0} {1}".format(d1,d2))
            
            return 1 + min(d1,d2)

    return deletion(str1,str2)


class TestCase(unittest.TestCase):
    
    def test_happy(self):
        self.assertEquals(deletion_distance("", "hola"), 4)
        self.assertEquals(deletion_distance("heat", "hit"), 3)



if __name__=="__main__":
    unittest.main().result
