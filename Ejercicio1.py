import numpy

# Crear array1
array1 = numpy.array([1, 2, 3, 4])
print("Array1: ", array1)

# Crear array2
array2 = numpy.array([[5, 6, 7, 8], [76.4, 23.5, 12.3, 45.6]], dtype="float64") # tambien vale .astype(numpy.float64)
print("Array2: ", array2)

# Crear array3
array3 = numpy.array([1,2,3,4,]).reshape(4,1) 
# tambien vale .reshape(4,-1) o .reshape(-1,1) 
# -1 es autocompletar el numero de filas o columnas
print("Array3: ", array3)

# Crear array con diagonal
diagonal = numpy.diag(range(50))
print("Diagonal: ", diagonal)
print("numero de elementos: "+str(diagonal.size))
print("numero de dimensiones: "+str(diagonal.ndim))
print("forma: "+str(diagonal.shape))
print("tipo de dato: "+str(diagonal.dtype))