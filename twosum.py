def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 0
        for x in nums:
            j = 0
            for y in nums:
                if (i != j) & (x + y == target):
                    print str(x) + " inedx("+ str(i)+ ") + "+ str(y)+ " inedx(" + str(j) + ") = " + str(target)
                    return [i,j]
                j += 1
            i += 1

if __name__ == "__main__":
    print(twoSum([3,2,4],6))
    print("hello world")
     
