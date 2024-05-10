class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_str = len(s)
        vowels_place = []
        vowels = []
        
        for i in range(len_str):
            if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
                vowels_place.append(i)
                vowels.append(s[i])
        

        new_str = ""
        v = len(vowels) - 1
        for i in range(len_str):
            if i in vowels_place: #searches vowels_place
                new_str += vowels[v]
                v -= 1
            else:
                new_str += s[i]
        
        return new_str

            

