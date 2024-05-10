''' see these two sites -- by githika
https://leetcode.com/problems/contains-duplicate/ 
https://neetcode.io/practice '''

def solution(lst):
  dict = {}
  for x in lst:
    if x in dict.keys():
      return True #bc x is already in dict
    else:
      dict[x] = 1
  return False
  
  
lst = [1,4,3]
print(solution(lst))
