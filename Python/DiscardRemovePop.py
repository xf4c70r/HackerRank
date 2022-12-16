n = int(input())
a_set = set(map(int, input().split()))
c = int(input())
for _ in range(c):
    t = input().split()
    if 'remove' in t:
        if int(t[1]) not in a_set:
            continue 
        a_set.remove(int(t[1]))
    elif 'discard' in t:
        a_set.discard(int(t[1]))
    elif 'pop' in t:
        a_set = set(sorted(a_set, reverse = True))
        a_set.pop()
        a_set = set(sorted(a_set, reverse = True))
    else : 
        pass
print(sum(a_set))