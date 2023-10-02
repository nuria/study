#!/usr/local/lib
import unittest

def highlite(query, result):
    
    q = list(query)
    hl_text = result
    
    lq = len(query)

    for i in range(0, len(result)-lq):
        # start comparing at zero 
        if result[i:i+lq] == query:
            hl_text = hl_text[0:i]+ "<b>"+ query+"</b>"+hl_text[i+lq:]

    return hl_text



class TestCase(unittest.TestCase):
    def test_happy_case(self):
        self.assertEqual(highlite("read", "reading is fun"), "<b>read</b>ing is fun")

        self.assertEqual(highlite("read", "reading is fun, do read"), "<b>read</b>ing is fun, do read")

if __name__=="__main__":
    unittest.main().result




