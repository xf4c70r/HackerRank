#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#

def appendAndDelete(s, t, k):
    
    lens = len(s)
    lent = len(t)
    maxi = max(lens,lent)
    mini = min(lens,lent)
    diff= maxi - mini
    count = 0
    if diff > k : 
        return 'No'
    else:
        for i in range(mini):
            if s[i] != t[i]:
                 count += 2*(mini - i) + diff
                 break
    if count == 0 :
        if maxi > mini :
            if 2*mini + diff > k:
                if (k - diff) // 2 > 0 and (k - diff) % 2 == 0 :
                    return "Yes" 
                else:
                    return "No"
    if count > k:
        return "No"
    else:
        return "Yes"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
