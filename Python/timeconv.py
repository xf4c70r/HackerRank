#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    s_new = s[:8]
    s_format = s[8:]
    lst = s_new.split(':')
    x = lst.pop(0)
    x = int(x)
    if(s_format == 'PM' and x != 12):
        x += 12
        x = str(x)
    elif(s_format == 'PM' and x == 12):
        return(s_new)
    elif(s_format == 'AM' and x == 12):
            x -= 12
            x = str(x)
            if x == '0':
                x += "0"
    else:
        return(s_new)
    lst.insert(0,x)
    return(':'.join(lst))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
