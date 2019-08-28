import numpy as np

a = np.zeros(3) #se crea matriz de 1x3 de ceros
print a
z = np.zeros(10) #se crea matriz de 1x3 de ceros
print z
z.shape = (10,1) #cambia la matriz z a una de 10x1
print z
z = np.ones(10) #cambia la matriz a una de 1x10 de 1s
print z
z = np.empty(3) #cambia la matriz a una de 1x3 de ceros
print z
z = np.linspace(2, 10, 5) #crea un arreglo del 2 al 10 con 5 elementos
print z
z = np.array([10,20]) #se crea arreglo de una lista
print z
a_list = [1,2,3,4,5,6,7] #crea lista
z = np.array([a_list]) #crea arreglo de la lista
print z
print type (z)
b_list = [[9,8,7,6,5,4,3],[1,2,3,4,5,6,7]]
z = np.array([b_list])
print z.shape #imprime las dimensiones de la matriz
np.random.seed(0) #se genera una referencia para el random
z1 = np.random.randint(10, size = 6) # se hace un random con las dimensiones 1x6 y con valores entre 0 y 10
print z1
print z1[0]
print z1[0:2]
print z1[-1]

