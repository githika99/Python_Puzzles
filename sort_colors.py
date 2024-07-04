# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        In place means that the no additional space should be allocated to sort. 
        """
        
        # solution! count how many 0s, 1s, and 2s
        z = 0
        o = 0
        t = 0
        for i in nums:
            if i == 0:
                z+= 1
            elif i == 1:
                o += 1
            else:
                t +=1
        
        #make the first z places 0, 
        for i in range(len(nums)):
            if i < z:
                nums[i] = 0
            elif i < o+z:
                nums[i] = 1
            else:
                nums[i] = 2
        
        return nums
