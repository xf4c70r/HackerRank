#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(n,arr):
    sum_1 = 0
    sum_2 = 0
    l = len(arr[0])
    for i in range (n):
            for j in range (n):
                if i == j:
                    sum_1 += arr[i][j]
    for i in range (n):
        sum_2 += arr[i][l-i-1]
    diff = abs(sum_1 - sum_2)
    return diff
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(n,arr)

    fptr.write(str(result) + '\n')

    fptr.close()
