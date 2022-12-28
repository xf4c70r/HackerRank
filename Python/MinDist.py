#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    
    min_distance = len(a)
    d = {}
    for i in range(len(a)):
        b = a[i]
        if b in d.keys():
            min_distance = min(min_distance, i - d[b])
            if min_distance == 1:
                break
        d[b] = i

    return min_distance if min_distance < len(a) else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
