if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    int_t = tuple(integer_list)
    print(hash(int_t))