"""Problem Merge Strings Alternately"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        #merge sort
        len1 = len(word1)
        len2 = len(word2)
        i = 0
        j = 0
        newstr = ""
        is_word1 = True
        while True:
            if is_word1 and i < len1:
                newstr += word1[i]
                i += 1
                is_word1 = False
            elif not is_word1 and j < len2:
                newstr += word2[j]
                j += 1
                is_word1 = True
            else:
                break


        if is_word1:                #means word1 is over
            newstr += word2[j:]

        elif not is_word1:                #means word1 is over
            newstr += word1[i:]

        return newstr
            
