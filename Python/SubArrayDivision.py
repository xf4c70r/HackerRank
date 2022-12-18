#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    counter = 0
    for i in range(len(s)):
        if sum(s[i:m + i]) == d:
            counter += 1
    return counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
