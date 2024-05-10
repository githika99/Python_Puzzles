import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    lst = x.copy()
    lst.sort()
    print(lst)
    # Write your code here
    transmitters = 1
    # Count # of groups that are 2k away from each other
    group_start_index = 0
    group_start_val = lst[0]
    last_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] - group_start_val <= (2 * k) and lst[i] - last_val <= k:
            last_val = lst[i]
        else:
            print("group is", group_start_val, "to", lst[i-1])
            #make a new group
            transmitters += 1
            group_start_index = i
            group_start_val = last_val = lst[i]
    print("group is", group_start_val, "to", lst[-1])
    return transmitters
        


if __name__ == '__main__':
    print("NEW HACKERLAND")
    count = 0
    with open('input_for_hackerland.txt') as f:
        for line in f:
            print("entered read loop")
            if count == 0:
                first_line = line.rstrip().split()

            if count == 1:
                second_line = line.rstrip().split()
                print("in second line")

            count += 1

    n = int(first_line[0])
    k = int(first_line[1])
    print("n is", n, "k is", k)
    x = list(map(int, second_line))
    result = hackerlandRadioTransmitters(x, k)

    print("RESULT IS", result)

