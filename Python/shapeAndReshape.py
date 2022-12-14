import numpy

def arrays(arr):
    l = list()
    for x in arr:
        l.append(int(x))
    a = numpy.array(l).reshape(3,3)
    return(a)
    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
