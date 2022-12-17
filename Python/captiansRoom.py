K = int(input())
Rooms = list(map(int,input().split()))
RoomNum = set(Rooms)

IdealRoomTotal = sum(RoomNum)*K
RealRoomTotal = sum(Rooms)

CaptainRoom = (IdealRoomTotal-RealRoomTotal)//(K-1)
print(CaptainRoom)

"""
Another Method : 

n = int(input())
a = list(map(int, input().split()))
freq = {}
for item in a:
    if (item in freq):
        freq[item] += 1
    else:
        freq[item] = 1

for key, value in freq.items():
    if value == 1:
        print(key)

"""