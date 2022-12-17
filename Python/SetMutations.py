n=int(input())
A=set(map(int,input().split()))
m=int(input())
for i in range(m):
    s=input().split()
    M=set(map(int,input().split()))
    if(s[0]=='update'):
        A|=M
    elif(s[0]=='intersection_update'):
        A&=M
    elif(s[0]=='difference_update'):
        A-=M
    elif(s[0]=='symmetric_difference_update'):
        A^=M
print(sum(A))