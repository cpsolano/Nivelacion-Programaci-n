import numpy as np
a = np.arange(10) #arreglo del 0 al 9
print a
np.random.shuffle(a) #cambia el orden de los valores
print a
print np.random.choice(a) #imprime valor al azar dentro de a
print np.random.random_integers(5,10,2) #2 valores al azar entre 5 y 10