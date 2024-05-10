# solution works but fails to pass time limit 
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
    #make each player make the most optimal moves
        len_s = len(senate)
        #do this until senate has only Rs or only Ds (repeat)
        #first iterate after x
        #if not found, iterate before x 
        while True:
            len_s = len(len_s)
            for x in range(len_s):
                if senate[x] == 'R':
                    y_found = False
                    for y in range(x+1, len_s):
                        if senate[y] == 'D':
                            senate = senate[:y] + "X" + senate[y+1:]
                            print (senate)
                            y_found = True
                            break
                    if not y_found:
                        for y in range(0, x):
                            if senate[y] == 'D':
                                senate = senate[:y] + "X" + senate[y+1:]
                                print (senate)
                                y_found = True
                                break
                        
                    if not y_found:                 #no Ds in senate
                        return "Radiant"
                        
                elif senate[x] == 'D':
                    y_found = False
                    for y in range(x+1, len_s):
                        if senate[y] == 'R':
                            senate = senate[:y] + "X" + senate[y+1:]
                            y_found = True
                            print (senate)
                            break
                    if not y_found:
                        for y in range(0, x):
                            if senate[y] == 'R':
                                senate = senate[:y] + "X" + senate[y+1:]
                                print (senate)
                                y_found = True
                                break
                    if not y_found:                 #no Rs in senate
                        return "Dire"
                