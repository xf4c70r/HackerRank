#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    
    if len(s) ==1:
        if s[0]=='a':
            return n
    count = 0
    for i in s:
        if i == 'a':
            count+=1
    sus = n//len(s)
    count = count*sus
    for i in s[:n-(sus*len(s))]:
        if i == 'a':
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
