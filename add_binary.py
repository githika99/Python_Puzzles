# PROBLEM 2 : adding binary
# Understand
  #Should we jutify the numbers to the right or left?
    # Right
  # Can adding two binary numbers have a carry?
    # Yes, adding a 1 and a 1 has an answer of 2, 2 in binary is '10', so the ans is 0 and the carry is 1. 
    # Adding 1 + 1 + 1 = 3, which in binary is '11' so the answer is 1 and carry is 1. 

# Match
  # iterate through lists from end (right side)

# Plan
  # iterate through lists from end (right side) and add each pair of characters and the carry. 

# Implementaion
def addBinary(self, a: str, b: str) -> str:
  c1 = len(a) -1
  c2 = len(b) - 1
  ans = ""
  carry = 0
  while c1 >= 0 or c2 >= 0 or carry > 0:
      if c1 >= 0 and c2 >= 0:
          temp = int(a[c1]) + int(b[c2]) + carry
      elif c1 >= 0:
          temp = int(a[c1]) + carry
      elif c2 >= 0:
          temp = int(b[c2]) + carry
      else:
          ans = str(carry) +ans
          return ans

      c1 -= 1
      c2 -= 1

      if temp == 1:
          carry = 0
      elif temp == 2: #binary '10'
          carry = 1
          temp = 0
      elif temp == 3: #binary '11'
          carry = 1
          temp = 1

      ans = str(temp) +ans #add to the beginning of ans

  return ans

# Review
  # Time complexity: O(n) where n is the length of whichever string is longer, a or b
  # Space complexity: O(n) where n is the length of whichever string is longer, a or b

