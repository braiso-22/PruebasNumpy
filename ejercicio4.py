import numpy

array3x3 = numpy.zeros((3,3))
largo_diagonal = range(array3x3.shape[0])
diagonal = (largo_diagonal,largo_diagonal)
array3x3[diagonal] = 1
print(array3x3)

array44 = numpy.random.randint(1, 75, (4,4))

diagonal = numpy.eye(4, dtype="bool")
array44[diagonal] = 50
print(array44)

array44[numpy.where(array44 < 50)] = 0
print(array44)

array44[numpy.where(array44 > 50)] = 100
print(array44)