import numpy
'''
    Genera una matriz de numeros y obten todos los números impares
'''
print("todos: ")
todos = numpy.array(range(10, 22)).reshape(3, -1)
print(todos)

print("impares: ")
impares = todos[todos % 2 == 1]
print(impares)

'''
    encuentra la posicion de los elementos pares en el array
'''
print("posicion: ")
posiciones_fila_columa = numpy.where(todos % 2 == 0)
print(posiciones_fila_columa)

'''
    Suma a los elementos pares 1
'''
print("suma a impares: ")
todos[posiciones_fila_columa] += 1
print(todos)
