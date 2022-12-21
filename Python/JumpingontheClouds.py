#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    
    e = 100
    n = len(c)
    li = []
    if n%k == 0:
        for i in range(0, n, k):
            if c[i] == 1:
                e -= 2
        return int(e - n/k)
    else:
        for i in range(n):
            if c[(i+k)%n] == 1:
                e -= 2
        return e - n
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
