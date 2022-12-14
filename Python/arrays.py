import numpy

def arrays(arr):
    l = list()
    for x in arr:
        l.append(float(x))
    a = numpy.array(l)
    return(a[::-1])
    

