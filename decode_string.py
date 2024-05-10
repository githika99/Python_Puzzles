class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_lets = ""
        output = ""
        for x in s:
            if 48 <= ord(x) and ord(x) <= 57:       #is a digit

                if curr_lets != "" and curr_num != 0:                 #if num is detected before ] is detected (nested)
                    stack.append(curr_num)
                    stack.append(curr_lets)
                    curr_lets = ""
                    curr_num = 0

                if ord(x) == 48:                    #x == '0'
                    curr_num = curr_num * 10

                else:
                    curr_num = curr_num * 10 + int(x)

            elif 97 <= ord(x) and ord(x) <= 122:    #is a letter
                if curr_num == 0:   #left over letters
                    output += x
                else:
                    curr_lets += x
            elif ord(x) == 93:                    #we reach ] 
                print (curr_num, curr_lets)
                if not stack:
                    output += curr_num * curr_lets
                else:
                    #do nested thing
                    curr_lets = curr_num * curr_lets
                    while stack:
                        stack[-1] += curr_lets
                        curr_lets = stack[-2] * stack[-1]
                        stack.pop()
                        stack.pop()
                    output += curr_lets
                        
                #reset
                curr_lets = ""
                curr_num = 0
        
        return output
