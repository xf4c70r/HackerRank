import numpy
polymonial = numpy.array(input().strip().split(), float)
x = float(input())
print(numpy.polyval(polymonial, x))
