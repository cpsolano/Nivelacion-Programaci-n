import numpy as np
a = np.arange(25).reshape(5,5) #secrea arreglo hasta el 25 exclusive con 5 valores por fila y un total de 5 filas
print a
print a % 3 #muestra como 0 los valores divisibles por 3
print a % 3 == 0 #muestra como True todos los valores que sean divisibles por 3
print a[a%3 == 0] #muestra los valores divisibles por 3

output = np.empty_like(a, dtype = "float") #se crea un array vacio tipo float con las dimensiones de a
output.fill(np.nan) #se llena output de nan
mask = a%3 == 0
output[mask] = a[mask]
print a
print output


