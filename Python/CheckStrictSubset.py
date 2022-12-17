A=set(map(int,input().split()))
n=int(input())
count = 0
for _ in range(n):
    B=set(map(int,input().split()))
    if (B.issubset(A)):
        count += 1
if count == n :
    print('True')
else:
    print('False')