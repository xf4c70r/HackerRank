import numpy
numpy.set_printoptions(legacy = '1.13')
a = input().strip().split()
array = [float(x) for x in a]
print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))
