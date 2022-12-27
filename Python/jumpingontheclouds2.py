#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    
    i = 1
    steps = 0
    while i<len(c):
        try:
            if c[i+1]!=1:
                i = i+2
                steps= steps+1
            else:
                i = i+1
                steps += 1
        except:
            i=i+1
            steps +=1
    return steps
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
