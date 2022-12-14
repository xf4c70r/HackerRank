import os
import sys

def miniMaxSum(arr):
    mini_and_maxi = []
    x = sum(arr)
    for i in range(len(arr)):
        total = 0
        total = x - arr[i]
        mini_and_maxi.append(total)
    print(min(mini_and_maxi), max(mini_and_maxi))
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
