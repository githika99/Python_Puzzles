class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        #gives you k largest values of a list
        #and then the average of those 
        avg_list = [float('-inf')] * k
        avg_sum = 0
        p = 0
        for n in nums:
            print "in outer loop"
            p = min(avg_list)
            if n >= p:
                    print "we changed " +  str(p) + " to " + str(n)
                    avg_list.remove(p)
                    avg_list.append(n)
                    if not p == float('-inf'):
                        print "p is not -inf, p is " + str(p)
                        avg_sum -= p
                    avg_sum += n

            
        print(avg_list)
        return avg_sum/k
    
#don't remember which version of solution this is
#gives you k largest values of a list
        #and then the average of those 
        avg_list = [float('-inf')] * k
        avg_sum = 0                         #fix so that it is not 0
        curr_avg = 0
        for n in range(len(nums)):
            for i in range(1,k):
                if n + k < len(nums):
                    break
                #add k 
            print "in outer loop"
            p = min(avg_list)
            if n >= p:
                    print "we changed " +  str(p) + " to " + str(n)
                    avg_list.remove(p)
                    avg_list.append(n)
                    if not p == float('-inf'):
                        print "p is not -inf, p is " + str(p)
                        avg_sum -= p
                    avg_sum += n

            
        print(avg_list)
        return avg_sum/k