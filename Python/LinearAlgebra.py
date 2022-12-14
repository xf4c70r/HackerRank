import numpy
n = int(input())
array = numpy.array([input().strip().split() for _ in range(n)], float)
print(round(numpy.linalg.det(array), 2))
