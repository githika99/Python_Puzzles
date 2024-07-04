# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        ans_r = [0] * len(nums)

        # without division
        # 2 pointers! 

        # calculate product to left
        p = 1 # starts as 1
        for i in range(len(nums)):
            ans[i] = p
            p *= nums[i]
        
        print("left sums", ans)
        
        # calculate product to right
        p = 1
        for i in range(len(nums)-1, -1, -1): #reverse order
            ans_r[i] = p
            ans[i] *= p
            p *= nums[i]
        
        print("right sums", ans_r)

        return ans
    
        
        # division solution
        # find total product
        # at each num divide by i
        # if i == 0, don't divide
        
