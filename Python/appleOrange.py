#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_lst = []
    oranges_lst = []
    for ap in apples:
        d = a + ap
        if d >= s and d<= t:
            apples_lst.append(d)
    for o in oranges:
        d = b + o
        if d >= s and d<= t:
            oranges_lst.append(d)
    print(len(apples_lst))
    print(len(oranges_lst))
             
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
