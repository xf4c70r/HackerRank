#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def median(size, values):
    if size % 2 == 0:
        median = (values[int(size/2)-1] + values[int(size/2)]) / 2
    else:
        median = values[int(size/2)]
    return int(median)

def quartiles(size, arr):
    arr.sort()
    L_h = list()
    U_h = list()
    mid = list()
    
    # Write your code here
    if size % 2 == 0:
        L_h = arr[0:int(size/2)]
        U_h = arr[int(size/2):size]
    else:
        L_h = arr[0:int(size/2)]
        U_h = arr[int(size/2)+1:size]
    return(median(len(L_h), L_h), median(size, arr), median(len(U_h), U_h))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))
    res = quartiles(n, data)
    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
