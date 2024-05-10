# code submits, but i want to improve it 
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        curr_sum = 0
        len_n = len(nums)
        zeros = 0
        for i in range(len_n):      #0 to k-1
            if nums[i] == 1:
                curr_sum += 1
            elif nums[i] == 0 and zeros < k:
                curr_sum += 1
                zeros += 1
            else:
                break
        #print "curr_sum is " + str(curr_sum) + " zeros is " + str(zeros)
        max_sum = curr_sum
        i = 1
        while i <= len_n - curr_sum:
            #print ()
            #print "starting at i = " + str(i) + " zeros is " + str(zeros)
            if nums[i-1] == 1:
                curr_sum -= 1
            elif nums[i-1] == 0 and zeros > 0:
                curr_sum -= 1
                zeros -= 1
                #print "zero is removed at " + str(i-1)

            for n in range(i+curr_sum, len_n):      #0 to k-1
                if nums[n] == 1:           #used to be nums[i+curr_sum-1+n]
                    curr_sum += 1
                elif nums[n] == 0 and zeros < k:
                    curr_sum += 1
                    zeros += 1
                    #print "zero is added at " + str(n)
                else:
                    break
           
            #print "curr_sum is " + str(curr_sum)
            if curr_sum > max_sum:
                max_sum = curr_sum
            i += 1
        return max_sum