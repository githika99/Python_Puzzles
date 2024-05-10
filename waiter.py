# problem: Waiter, Hackerrank Intermediate Stacks
# link: https://www.hackerrank.com/challenges/one-month-preparation-kit-waiter/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-three

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number (list)
#  2. INTEGER q (number of iterations)
#

def waiter(number, q):
    # Write your code here
    # first get a list of first q prime numbers
    # only need to find prime numbers that are equal to or smaller than max of list
    # m = 0
    # for i in number:
    #     m = max(m, i)
    
    primes = []
    for i in range(2, 10000):
        valid = True
        for j in range(2, int(i/2 + 1)):
            if i % j == 0:
                valid = False
                break
        if valid:
            primes.append(i)

    print("primes is", primes)
    
    ans = []
    A = []
    B = []
    for i in range(q):
        while (number):
            p = number.pop()
            if p % primes[i] == 0:
                B.append(p)
            else:
                A.append(p)
        while (B):
            ans.append(B.pop())
        number = A
        A = []
    #append in backwards order
    while (number):
        ans.append(number.pop())
    print("ans is now", ans)
    return ans
    
    """
    Pseudo code:
    Treat all as stacks, not as arrays
        First pop from number and append to B  or A if whatever
        Then pop from B and append to ans
        Then make number = A
        Then make A an empty stack
        Once you've done i iteratins, pop from number and append to ans
    """
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
