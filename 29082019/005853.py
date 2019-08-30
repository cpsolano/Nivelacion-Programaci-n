import numpy as np
a = np.array([3,-1,-2,4,-6,8])
negatives = a < 0 #define negatives como los valores de a menores a 0
print a[negatives]
a[negatives] = 0 #reemplaza los valores que cumplen con la condiciones de negative por ceros
print a

#& (and), | (or), ~ (not)
print (a > 3) & (a < 8) # se muestran como true los valores que cumplen ambas condiciones


