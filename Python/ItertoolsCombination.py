from itertools import combinations

a=list(input().split())
n = int(a[-1])
for i in range(1, n+1): 
    print(*["".join(s) for s in list(combinations(sorted(a[0]),i))],sep="\n")