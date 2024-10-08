# PROBLEM 1 

# Understand
  # Can the substring be the whole original string?
    # Yes
  # Can the substring be longer than the original string?
    # No

# Match
  # Iterate through Strings with Pointer for Indices

# Plan
  # We can go through the first string, and if the character at that index equals the first char of the second string, we can loop through the rest of the characters of both strings. if this results in the second string's counter = len of the second string, then we can return true. otherwise, we can subtract the first string's counter by whatever we incremented it by, add 1, and continue in the big loop. outside the big loop, return false. 

# Implement
def solution (str1, str2):
  i = 0
  while i < len(str1):
    print("i = ", i)
    j = 0
    offset = 0
    while i < len(str1) and j < len(str2):
      print("j start", j, "i start", i)
      if str1[i] != str2[j]:
        print("break")
        break
      offset += 1
      i += 1
      j += 1
      print("j end", j, "i end", i)
    print("i", i, "j", j)
    if j == len(str2):
      return True
    i -= offset
    i += 1

  return False

print(solution("hello", "el"))

# Review
    # Time: This problem has a worst case time complexity of O(N*M), since we could loop through M characters at any point in str1, as long as there are M characters left in str1 
    # Space: O(1)
