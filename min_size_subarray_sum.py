def givemewhatiwant(str):
     lst = str.split(', ')
     for x in lst:
          print(x)
     return


def minSubArrayLen(target, nums):

        if sum(nums) < target: return 0               # <-- 1

        s, l, ans = 0, 0, len(nums)                   # <-- 2
        
        for r,val in enumerate(nums):                 # 
            s+= val                                   #
            while s >= target:                        # <-- 3
                s-= nums[l]                           #
                ans = min(ans, r - l + 1)             #
                l+= 1                                 #

        return ans        

if __name__ == "__main__":
     #minSubArrayLen(7, [2,3,1,2,4,3])
     givemewhatiwant('American Express, Visa, Wells Fargo, Bank of America, discover, masrtercard, citibank, chase, barclays, US Bank, synchrony bank, USAA, credit one, axis bank, JCD Co. Ltd., Navy Federal Credit union')