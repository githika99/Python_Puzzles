# edit
"""Product of an Array Except Self"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = []
        product = 1

        #only for cases in which there is no 0
        for c in range(len(nums)):
            product *= nums[c]
        if product != 0:
            for c in range(len(nums)):
                products.append(product/nums[c])
            return products

        #for cases in which there is a 0
        for c in range(len(nums)):
            product = 1
            for i in range(len(nums)):
                if i != c:
                    product *= nums[i]
            products.append(product)
        
        return products
    
"""Really good solution I saw on Leet Code"""
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left_product = [1] * n # initialize left_product array with 1
        right_product = [1] * n # initialize right_product array with 1

        # calculate the product of elements to the left of each element
        for i in range(1, n):
            left_product[i] = left_product[i - 1] * nums[i - 1]
            #range is (1,n) bc we start at 1 (the 0th position's left multiple must be 1 
            #(or 0, but if it is 0 it will be multiplied by 0 later anyways so it's okay))
        print left_product

        # calculate the product of elements to the right of each element
        for i in range(n - 2, -1, -1):
            right_product[i] = right_product[i + 1] * nums[i + 1]
            #range is (n-2, -1, -1) bc we start at last element, and go till 0 bc range 
            #never goes to the last one
        
        print right_product

        # calculate the product of all elements except nums[i]
        result = [left_product[i] * right_product[i] for i in range(n)]

        return result
