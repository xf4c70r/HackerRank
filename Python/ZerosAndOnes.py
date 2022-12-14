import numpy

arr = input().strip().split()
dim = [int(x) for x in arr]
print(numpy.zeros((dim), dtype = numpy.int))
print(numpy.ones((dim), dtype = numpy.int))
