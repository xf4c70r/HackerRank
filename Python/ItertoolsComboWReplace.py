from itertools import combinations_with_replacement

a=list(input().split())
n = int(a[-1])
print(*["".join(s) for s in list(combinations_with_replacement(sorted(a[0]),n))],sep="\n")