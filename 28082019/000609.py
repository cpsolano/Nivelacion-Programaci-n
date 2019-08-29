import numpy as np

a = np.array([2,3,4]) #arreglo con los valores entregados
print a
a = np.arange(1,12,2) #arreglo con valores entre 1 y 12 con salto de 2
print a
a = np.linspace(1,12,6)  #arreglo con 6 valores entre 1 y 12 equiespaciados
print a
a.reshape(3,2) #transforma a matriz de 3x2
print a.size #cantidad de valores
print a.dtype #muestra el tipo de a

b = np.array([(1,5,2,3),(4,5,6)]) #se crea matriz de 1x2

print a < 4 # imprime la matriz con true o false
print a * 3 #multiplica los valores de a por 3 pero no modifica a
a *= 3 #multiplica los valores de a y modifica el arreglo
print a

a = np.zeros((3,4)) #arreglo de 3x4 de ceros
print a
a = np.ones ((2,3)) #arreglo de 2x3 de unos
print a
a = np.ones(10) #arreglo de 1x10
print a
a = np.array([2,3,4], dtype = np.int16) #permite cambiar el tipo de a
print a
a = np.random.random((2,3)) # valores al azar entre 0 y 1
print a
a = np.random.randint(0,10,5) #5 valores al azar entre 0 y 10
print a
print a.sum() #entrega suma total de los valores de a
print a.min() #valor minimo
print a.max() #valor maximo
print a.mean() #promedio
print a.var() #varianza
print a.std() #desv estandar

a = np.random.randint(1,10,6)
a = a.reshape(3,2) #ajusta los valores de a a una matriz de 3 filas con dos valores cada una
print a.sum(axis=1) #hace la suma de cada fila
print a.sum(axis=0) #suma los valores de forma vertical
