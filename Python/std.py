#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(n, arr):
    # Print your answers to 1 decimal place within this function
    mean = sum(arr)/n
    dev = list()
    for i in arr:
        dev.append((i - mean)**2)
    return(round((sum(dev)/n)**(1/2), 1))
    

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    print(stdDev(n, vals))
