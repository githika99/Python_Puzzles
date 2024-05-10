class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        j = 1
        k = 2
        if len(nums) < 3:
            return False

        found_j = False
        for n in range(len(nums)):      #n goes from 0 to len(nums - 1)
            for c in range(n, len(nums)): 
                if nums[c] > nums[n]:
                    for x in range(c, len(nums)): 
                        if nums[x] > nums[c]:
                            i = n
                            j = c
                            k = x
                            print "i is " + str(i) + "nums[i] is " + str(nums[i])
                            print "j is " + str(j) + "nums[j] is " + str(nums[j])
                            print "k is " + str(k) + "nums[k] is " + str(nums[k])
                            return True

        
"""really good solution on leet code"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        print str(first)
        print str(second)
        for n in nums:
            if n <= first:
                print "first is now " + str(n)
                first = n
            elif n <= second:
                print "second is now " + str(n)
                second = n
            else:
                return True
        return False

        
            
        
        