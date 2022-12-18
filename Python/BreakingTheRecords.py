#!/bin/python3

import math
import os
import random
import re
import sys


def breakingRecords(scores):
    
    min_score = scores[0]
    max_score = scores[0]
    min_record = 0
    max_record = 0
    
    for i in range(1, len(scores)):

        if scores[i] < min_score:
            min_record += 1
            min_score = scores[i]
            
        elif scores[i] > max_score:
            max_record += 1
            max_score = scores[i]
    return [max_record, min_record]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
