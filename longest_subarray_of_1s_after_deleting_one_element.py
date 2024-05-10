def longestSubarray(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_n = len(nums)
        max_sum, cnt, l, removed, start = 0, 0, 0, 0, 0
        
        #let's say we already have some number cnt

        while start < len_n-1:
            l = start + cnt
            if start != 0:
                if nums[start-1] == 1:        #if it was 0, we don't need to remove cnt
                    cnt -= 1
                else:        #if it was 0, we don't need to remove cnt
                    removed -= 1
            for key in range(l, len_n):                    
                if nums[key] == 0:
                    if removed == 0:
                        removed += 1
                        l += 1
                    else:
                        break               #break if we encounter a 0 and we already removed one 0 
                                            #or break if we reached end of list
                else:                             
                    cnt += 1
                    l += 1

                if key == len_n-1 and removed == 0:       #we didn't remove anything, must delete 1
                    cnt -= 1

            print ("starting at " + str(start) + " yields " + str(cnt))
            max_sum = max(max_sum, cnt)
            start += 1
                
        return max_sum


if __name__ == "__main__":
     print(longestSubarray([0,1,1,1,0,1,1,0,1]))