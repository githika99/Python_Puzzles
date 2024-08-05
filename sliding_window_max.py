# https://leetcode.com/problems/sliding-window-maximum/solutions/4521064/simple-one-pass-solution/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = [nums[0]]

        for i in range(1,k):
            #if nums[i] <= queue[-1]:  
            #    queue.append(nums[i])
            #we can comment out those lines bc we always add the new number
            while queue and nums[i] > queue[-1]:    
                #if new num is greater than last in queue
                queue.pop()
            queue.append(nums[i])

        res.append(queue[0])

        for i in range(k, len(nums)):
            if nums[i-k] == queue[0]:
                queue.pop(0)
                
            while queue and nums[i] > queue[-1]:    
                #if new num is greater than last in queue
                queue.pop()
            queue.append(nums[i])
            res.append(queue[0])
            
        return res

        """
    idea:   
            maintain a queue where each element is smaller than the one before
            delete a number if it exits the subarray
            delete a number if the next number in the subarray is bigger than it

    implementation:
        go from beginning to k and add to queue if it is smaller than or equal to before.
            if bigger than top of queue, pop until that's not true
        add front of queue to res
        go through rest of list. if nums[i-k] == front of queue, 
            delete from front of queue
        add new num to queue on same conditions
        add front of queue to res

        return res
        """
