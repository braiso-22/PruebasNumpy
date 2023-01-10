import numpy

# multiplicar 2 matrices
array= numpy.diag(range(4))
print(array)
array2 = numpy.array(range(16)).reshape(4,4)
print(array2)

array3 = array.dot(array2)
print(array3)