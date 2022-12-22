#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    
    dp = [1]*(n+1)
    dp[0] == 1
    dp[1] == 2
    for i in range(2,n+1):
        dp[i] = i*dp[i-1]
    print(dp[n])
    
    """
    num = 1

    while (n != 0):
        num *= n
        n -= 1

    print(num) 
    """

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
