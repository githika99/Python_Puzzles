def canCompleteCircuit(gas, cost):

        length = len(gas)
        tot = 0
        for i in range(length):
            i = 3
            tot = gas[i]
            curr = i
            start = True
            curr %= length
            while tot > 0:                  
                tot -= cost[curr]
                if tot < 0:
                    break
                if not start and (curr+1)%length == i:
                    return i
                curr += 1
                curr %= length
                tot += gas[curr]
                start = False
            if tot > 0:
                return i
        
        return -1

if __name__ == "__main__":
    print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
