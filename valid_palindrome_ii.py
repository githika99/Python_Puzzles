# https://leetcode.com/problems/valid-palindrome-ii/description/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 2 pointer solution

        def isPalindrome(start, end, count):

            # here we can set the limit for how many we remove
            if count > 1:
                return False

            if s[start] != s[end]:
                # check skipping one on the start
                # and skipping one on the left
                return isPalindrome(start+1, end, count+1) or isPalindrome(start, end-1, count+1)

            else:
                # otherwise call it again (last call makes start == end)
                if start < end:
                    return isPalindrome(start+1, end-1, count)

                # if start is not less than end (start should == end at the point)
                # we have gone through the whole string, and its safe to return True
                else:
                    return True

        start = 0
        end = len(s) - 1
        return isPalindrome(start, end, 0)

        # the reason we have to make it another function is so that we can set the parameters
        # and call it recurisively

