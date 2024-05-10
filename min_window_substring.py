def minWindow(s, t):
        len_s = len(s)
        len_t = len(t)
        if len_t > len_s:
            return ""
        
        temp = t
        l = 0
        final_output = ""
        output = ""
        i = 0

        while l < len_s:
            while temp and i < len_s - l:
                output += s[i + l]
                if s[i + l] in temp:
                    temp = temp.replace(s[i + l], '', 1)       #removes that from t
                i += 1

            print("loop broke, temp is", temp, "i is", i, "output is", output, "l is", l)
            if l == 0 and temp:                                #we did not find a match
                return ""
            
            elif not temp:
                if not final_output or len(output) < len(final_output):
                    final_output = output

            temp = t
            output = ""

            l += 1
            i = 0
            while l < len_s and s[i + l] not in temp:
                l += 1

        return final_output
        
if __name__ == "__main__":
    minWindow("baAabbBBB", "Bbbb")