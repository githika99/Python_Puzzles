class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        #chars.append('')
        len_c = len(chars)
        s = ""
        curr_num = 1
        prev = chars[0]

        if len_c == 1:
            return 1
       
        for c in range(1, len_c):
            if chars[c] == prev:
                curr_num += 1

            else:                       #new char reached
                s += str(prev)
                if curr_num > 1:
                    s += str(curr_num)
                curr_num = 1
                if c != (len_c - 1):
                    prev = chars[c]

        s += str(chars[c])
        if chars[c] == prev:
            s += str(curr_num)
                
        len_s = len(s) - 1
        i = 0

        while i < len_c:
            if i <= len_s:
                chars[i] = s[i]
            else:
                chars.pop(i)
                len_c -= 1
                i -= 1
            i += 1
        
        return len(chars)