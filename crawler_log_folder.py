# https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # count how far we are from the main folder at any point
        dist = 0
        for i in logs:
            if i == "./":
                continue
            if i == "../":
                if dist > 0:
                    dist -= 1
                # do not subtract 1 if we are already at 0
            else:
                dist += 1
        
        if dist < 0:
            return 0

        return dist
