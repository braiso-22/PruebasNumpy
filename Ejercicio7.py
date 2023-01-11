import numpy
'''
3𝑥 + 4𝑦 − 𝑧 = 8
5𝑥 − 2𝑦 + 𝑧 = 4
2𝑥 − 2𝑦 + 𝑧 = 1
'''
A = numpy.array([
                [3, 4, -1],
                [5, -2, 1],
                [2, -2, 1]
                ])
B = numpy.array([
                [8],
                [4],
                [1]
                ])
determinanteA = numpy.linalg.det(A)
# if ternario con determinante para hacer la inversa
Ap = numpy.linalg.inv(A) if determinanteA != 0 else "NO HAY INVERSA"
# AX = B
# (A'A)X = A'B
# X = A'B
X = Ap @ B
print(X)



