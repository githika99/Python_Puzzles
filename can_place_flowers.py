class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #my solution works but is a bit complicated
        len_flow = len(flowerbed)
        #first count how many consecutive 0s there are
        total_flows = 0
        #consecutive_zeros = []
        curr_consecutive = 0
        one_reached = False
        
        #edge case
        if len_flow == 1:
            if flowerbed[0] == 0 or (flowerbed[0] == 1 and n == 0):
                return True
            return False

        for i in range(len_flow):
            if flowerbed[i] == 0 and (i == 0 or i == len_flow - 1):
                one_reached = False
                curr_consecutive += 2
            elif flowerbed[i] == 0:
                #print "at i = " + str(i) + "f[i] == 0"
                one_reached = False
                curr_consecutive += 1
            else:
                one_reached = True
            if (one_reached or i == len_flow - 1) and curr_consecutive != 0:
                #consecutive_zeros.append(curr_consecutive)
                if curr_consecutive % 2 == 0:
                    curr_consecutive -= 1
                total_flows += int(curr_consecutive/2)
                curr_consecutive = 0
        
        #print consecutive_zeros

        if total_flows >= n:
            return True
        return False
        



        