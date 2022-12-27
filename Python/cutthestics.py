#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    
    lst=[]
    while(len(arr)>=1):
        x= min(arr)
        lst.append(len(arr))
        temp=len(arr)
        for i in range(temp):
            arr[i] = arr[i]-x
        for i in range(temp):
            if 0 in arr:
                arr.remove(0)
    return lst

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
