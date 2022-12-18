from itertools import permutations

a=list(input().split())
n=int(a[-1])
print(*["".join(s) for s in list(permutations(sorted(a[0]),n))],sep="\n")