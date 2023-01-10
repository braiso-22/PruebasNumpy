import numpy

'''
    crear una matriz de 20 filas y 5 columnas con valores flotantes 
    equiespaciados en el intervalo cerrado de 1 a 10
'''

matriz = numpy.linspace(1, 10, 100, dtype="float64").reshape(20, 5)
print("equiespaciado: ")
print(matriz)

'''
    Crear un array 1D con valores aleatorios y distribucion normal
'''
normal = numpy.random.normal(1, 2, 128)
print("normal: ")
print(normal)

'''
    Un array 1D con 15 valores aleatorios de una muestra 1, X, 2
    donde la probabilidad de que salga 1 es 0.5, la probabilidad 
    de x es 0.3 y la probabilidad de 2 es 0.2
'''
moneda = numpy.random.choice(["1", "X", "2"], 15, p=[0.5, 0.3, 0.2]).reshape(5,3)
print("moneda: ")
print(moneda)