import numpy
n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
part_array = numpy.sum(array, axis = 0)
#print(part_array)
print(numpy.prod(part_array, axis = None))
