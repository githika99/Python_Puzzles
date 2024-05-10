"""Greatest Common Divisor of Strings"""

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        substr = ""
        longest_substr = substr
        dict1 = {"":[]}
        len1 = len(str1)
        len2 = len(str2)
        i = 0
        j = 0
        in_str1 = False
        in_str2 = False
        while i < len1 and j < len2:
            if str1[i] == str2[j]:      #we found a match!
                substr += str2[j]
                i += 1
                j += 1
            else:
                break

            #test to see if it is a substring of str1 and str2
            n = 1
            for n in range(len1):
                if n*substr == str1:
                    in_str1 = True
                    break
            if in_str1:
                print substr + " * " + str(n) + " = " + str1
                dict1[substr] = [1]
                in_str1 = False
            else:
                dict1[substr] = [0]

            n = 1
            for n in range(len2):
                if n*substr == str2:
                    in_str2 = True
                    break
            if in_str2:
                print substr + " * " + str(n) + " = " + str2
                dict1[substr].append(1)
                in_str2 = False
            else:
                dict1[substr].append(0)

        print(dict1)
        return substr

"""Best solution so far"""
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        substr = ""
        longest_substr = substr
        len1 = len(str1)
        len2 = len(str2)
        i = 0
        j = 0
        in_str1 = False
        in_str2 = False
        while i < len1 and j < len2:
            in_str1 = False
            in_str2 = False
            if str1[i] == str2[j]:      #we found a match!
                substr += str2[j]
                i += 1
                j += 1
            else:
                break
            #test to see if it is a substring of str1 and str2
            for n in range(max(len1 + 1, len2 + 1)):
                if n*substr == str1:
                    in_str1 = True
                if n*substr == str2:
                    in_str2 = True
                    
            if in_str1 and in_str2:
                longest_substr = substr
            

        return longest_substr
