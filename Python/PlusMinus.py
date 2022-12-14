#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    denominator = len(arr)
    negetive = []
    positive = []
    zero = []
    for i in arr:
        if i < 0:
            negetive.append(i)
        elif i > 0:
            positive.append(i)
        else:
            zero.append(i)
    neg_ratio = float(len(negetive)/denominator) 
    pos_ratio = float(len(positive)/denominator)  
    zer_ratio = float(len(zero)/denominator) 
    print("%.6f" % pos_ratio)
    print("%.6f" % neg_ratio)
    print("%.6f" % zer_ratio)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
