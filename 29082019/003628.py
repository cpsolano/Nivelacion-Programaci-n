import numpy as np

a = np.array([10,11,12,13,14])
print a[1:3] # toma el valor 2 hasta el 3
print a[1:-2] #parte desde el 2do valor y le elimina los ultimos 2
print a[-4:3] #parte "contando desde atras" hasta el 3er valor
print a[:3] #toma los valores hasta el 3er valor inclusive
print a[-2:] #toma los 2 ultimos valores
print a[::2] #toma el primer valor y va saltando cada 2

a = np.arange(25).reshape(5,5) #crea arreglo de 25 datos y los ordena en una matriz de 5 valores por cada fila y un total de 5 filas
print a
red = a[:, 1::2] #toda la columna 2 y 4
print red
yellow = a[-1] #toma los valores de la ultima fila
print yellow
blue = a[1::2, :3:2] #toma los valores de la segunda y 4ta fila de la primera y tercera columna
print blue

