def average(array):
    # your code goes here
    a_set = set(array)
    total = sum(a_set)
    length = len(a_set)
    average = total / length
    return(round(average, 3))
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)