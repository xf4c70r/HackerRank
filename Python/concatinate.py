import numpy
n, m, p = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
array_1 = numpy.array([input().strip().split() for _ in range(m)], int)
print (numpy.concatenate((array, array_1), axis = 0) )
