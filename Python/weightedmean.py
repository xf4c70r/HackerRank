#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here
    mix = list()
    for i in range(len(X)):
        mix.append(X[i]*W[i])
    return(round((sum(mix)/sum(W)), 1))

if __name__ == '__main__':
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))
    print(weightedMean(vals, weights))
