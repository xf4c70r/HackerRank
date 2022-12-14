def mean(n, num):
    return(round(sum(num)/n, 1))

def median(n, num):
    num.sort()
    if(n % 2 == 0):
        n_1 = num[n//2]
        n_2 = num[n//2 - 1]
        return(round((n_1 + n_2)/2, 1))
    else:
        return(round(num[n//2], 1))

def mode(num):
    num.sort()
    frequency = {}
    for value in num:
        frequency[value] = frequency.get(value, 0) + 1
    most_frequent = max(frequency.values())
    modes = [key for key, value in frequency.items()
                      if value == most_frequent]
    modes.sort()
    return min(modes)

n = int(input())
num = [int(x) for x in input().split()]
print(mean(n,num))
print(median(n,num))
print(mode(num))
