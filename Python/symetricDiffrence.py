m = int(input())
lis_a = input().split()
a_set = set(map(int, lis_a))
n = int(input())
lis_b = input().split()
b_set = set(map(int, lis_b))
c_set = list(a_set.symmetric_difference(b_set))
c = list(c_set)
c.sort()
for i in c:
    print(i)


"""
Another Method : 

m = int(input())
lis_a = input().split()
a = list(map(int, lis_a))
a_set = set(a)
n = int(input())
lis_b = input().split()
b = list(map(int, lis_b))
b_set = set(b)
c_set = a_set.symmetric_difference(b_set)
c = list(c_set)
c.sort()
for i in c:
    print(i)

"""