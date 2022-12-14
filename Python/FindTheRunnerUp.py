if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(list(arr)))
    arr = sorted(arr)
    print(arr[-2])