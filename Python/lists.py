if __name__ == '__main__':
    lst = list()
    inp = list()
    for _ in range(int(input())):
        inp = input().split()
        for i in range(1,len(inp)):
            inp[i] = int(inp[i])
        #print(inp)
        if inp[0] == 'insert':
            lst.insert(inp[1], inp[2])
        elif inp[0] == 'print':
            print(lst)
        elif inp[0] == 'remove':
            lst.remove(int(inp[1]))
        elif inp[0] == 'append':
            lst.append(inp[1])
        elif inp[0] == 'sort':
            lst.sort()
        elif inp[0] == 'pop':
            lst.pop()
        elif inp[0] == 'reverse':
            lst.reverse()
        
