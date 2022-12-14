import numpy

n, m = map(int, input().split())

array = numpy.array([input().strip().split() for _ in range(n)], int)
print (numpy.mean(array, axis = 1))
print (numpy.var(array, axis = 0))
print (round(numpy.std(array), 11))
