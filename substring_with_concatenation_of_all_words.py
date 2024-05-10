def findSubstring(s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        each_word = len(words[0])
        num_words = len(words)
        result_len = num_words * each_word
        curr_test = {}
        for x in words:
            curr_test[x] = 0
        start, end = 0, 0
        len_s = len(s)

        while start < len_s:
            while end < start + result_len:
                print ("substring is " + str(s[end:end+each_word]))
                if  s[end:end+each_word] in curr_test and curr_test[s[end:end+each_word]] == 0:            
                    print ("is in curr_test!")
                    curr_test[s[end:end+each_word]] = 1       
                    end += each_word
                    print ("start is " + str(start) + " end is now " + str(end))
                elif  s[end:end+each_word] in curr_test and curr_test[s[end:end+each_word]] == 1:
                    #reset
                    for x in curr_test:
                        curr_test[x] = 0
                    start = end
                else: 
                    start = end = end + each_word
                    #reset if there is a break
                    for x in curr_test:
                        curr_test[x] = 0        
                    break
                if end == start + result_len:
                    result.append(start)
                    #remove start word from dictionary
                    curr_test[s[start:start+each_word]] = 0
                    start = start + each_word
                    #not great bc we already calculated from start + each_word to end
                    break     
        
        return result

if __name__ == "__main__":
     print(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))