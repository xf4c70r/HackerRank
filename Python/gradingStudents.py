#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    grades_new = []
    for g in grades:
        if (g % 5 > 2 and g >= 38):
            g =- (-g//5)*5
            g = str(g)
            grades_new.append(g)
        else:
            g = str(g)
            grades_new.append(g)
    return(grades_new)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    
    fptr.write('\n'.join(map(str,result)))
    fptr.write('\n')

    fptr.close()
