import numpy
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
a_min = numpy.min(array, axis = 1)
print(numpy.max(a_min))
