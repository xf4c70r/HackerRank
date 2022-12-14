if __name__ == '__main__':
    x, k= map(int, input().split())
    P = input()
    z = eval(P.replace('x', str(x)))
    print(bool(z == k))
