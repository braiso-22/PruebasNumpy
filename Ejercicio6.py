import numpy
randomized = numpy.random.randint(1, 11, 1000)

unicos, counts = numpy.unique(randomized, return_counts=True)

print("respuestas unicas: " + str(unicos))
print("numero de votos por respuesta: " + str(counts))
print()

matriz = numpy.array([[1,9,3],[4,5,6],[7,8,9]])
print("Matriz:\n " + str(matriz))
determinante = numpy.linalg.det(matriz)
print("determinante: " + str(determinante))
print()

if determinante != 0:
    inversa = numpy.linalg.inv(matriz)
    print("la inversa es: \n" + str(inversa))
else:
    print("No hay inversa")

print(matriz  @ inversa) # igual al .dot()