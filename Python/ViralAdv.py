#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    
    total_likes = 0
    for day in range(1, n+1):
        if day == 1:
            likes = math.floor(5/2)
        else:
            likes = math.floor(likes * 3 / 2)
        total_likes = total_likes + likes
    return total_likes
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
