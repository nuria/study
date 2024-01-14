#!usr/local/bin
import unittest

"""
in this regex match '*' matches the char before
zero or more times
and '.' matches anything

"""

def match (original_text, pattern):
    # iterative solution?
    i = 0 # haystack index
    j = 0 # pattern

    DOT = '.'
    ASTERISK = '*'

    # regular expressions are defined recursively
    def _match(text, pattern,current_index=0, asterisk_match=None):
        print(f'{text} and pattern: {pattern}')

        # this might be an explosion of cases cause we have to look ahead if current char does not match
        if len(text)==0  and len(pattern) !=0:
            if asterisk_match is None:
                return False
            else:
                # asteriks match taht has ended
                return True
        elif len(pattern) == 0 and len(text)!=0:
            return False
        elif len(text) == 0 and len(pattern)==0:
            return True

        # we are matching in this scheme text[0:] against pattern[0:] if 1st char matches
        # if we have an asterisks we continue with pattern[0] but until when
        # else skip 1st char and match text[1: against pattern[0:]
        
        # we have 2 types of matches: exact and not
        # we need to cary prior char in case we are matching an asterisk?

        if text[0] == pattern[0] or pattern[0] == DOT:
            # exact match
            return _match(text[1:], pattern[1:], current_index+1)
        elif pattern[0] == ASTERISK:
            if asterisk_match is None:
                # figure out if prior char matches
                asterisk_match = original_text[current_index-1]
            
            if asterisk_match == text[0]:
                return _match(text[1:], pattern, current_index+1, asterisk_match)
            else:
                # we might have stopped matching the asterisk
                return _match(text, pattern[1:], current_index+1)

        return False

        

    return _match(original_text, pattern)

class TestCase(unittest.TestCase):
    def test_happy_case(self):
        self.assertEqual(match('aa','aa'), True)
        self.assertEqual(match('abc','a.b'), False)
        self.assertEqual(match('abc','a.c'), True)
        self.assertEqual(match('abbb','ab*'), True)
        self.assertEqual(match('aa','aba'), False)

        self.assertEqual(match('abbbC','ab*CC'), False)
        
        self.assertEqual(match('abbbC','ab*C'), True)


if __name__=="__main__":
    unittest.main().result
