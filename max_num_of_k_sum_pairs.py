class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #print nums
        len_n = len(nums)
    
        #print len_n
        additions = 0
        new_l = False
        new_r = 0
        l, r, curr = 0, len_n - 1, 0
        while l < r:
            while len(nums) > 1 and nums[l] >= k:
                nums.pop(l)
                r -= 1
                if l >= len(nums) - 1:
                    break
                #print "new l is " + str(l)
            while len(nums) > 1 and (nums[r] >= k):
                nums.pop(r)
                r -= 1
                if r == 1:
                    break
                #print "new r from loop 1 is " + str(r)
            
            if len(nums) <= 1:                              #if we removed too many numbers
                    break

            #print nums
            #print l, r
            curr = nums[l] + nums[r]
            if curr == k:
                additions += 1
                nums.pop(r)             #important that we pop right before left, so left index doesn't get mixed up
                nums.pop(l)
                #print "match found"
                r = len(nums) - 1
                #do we change value of l and r?

            elif curr > k:              #we need a smaller r
                #print "curr is too big, " + str(curr)
                new_r = r - 1           
                while l <= new_r and nums[new_r] >= nums[r]:
                    new_r -= 1
                #print "new r from loop 2 is " + str(r)
                r = new_r
                if r <= l:
                    new_l = True
            
            elif curr < k:              #we need a bigger r
                #print "curr is too small, " + str(curr)
                new_r = r - 1           
                while l <= new_r and nums[new_r] <= nums[r]:
                    new_r -= 1
                #print "new r from loop 3 is " + str(r)
                r = new_r
                if r <= l:
                    new_l = True

            if new_l:
                l += 1
                r = len(nums) - 1
                new_l = False
        
        return additions 