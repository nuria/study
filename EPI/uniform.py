!#/usr/local/bin

"""
A positive integer is considered uniform if all of its digits are equal. For example, 
222 is uniform, while 
223 is not.
Given two positive integers 
A and 
B, determine the number of uniform integers between 
A and 
B, inclusive.
"""

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here

  b = list(str(B)) # 75 => ['7','5']
  a = list(str(A))

  # there are 10 uniform numbers in each power of 10 , they are multiples of 1,11, 111


  d = len(a)
  tally = 0 
  
  _11 = int("".join(['1'] * d)) # will be 11,111, 1111
  while (_11 <B and d <= len(b)):
    # 11,111, 1111
    i = 1 
    candidate = _11 * i
    while i <= 9:
      if A <= candidate and candidate <= B:
        tally = tally + 1
        print(candidate)
      i = i + 1
      candidate = _11 * i 
    d = d + 1 
    _11= int("".join(['1'] * d))
  
  return tally

