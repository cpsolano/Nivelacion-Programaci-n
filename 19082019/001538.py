g = 9 #variable
h = 8 #variable
if g < h: #condicion inicial
    print "g is less than h" #lo que muestra la consola si se cumple la condicion anterior
else: #lo que ocurre si no se cumple la condicion inicial
    if g == h: #nueva condicion "inicial" dentro del else
        print "g is equal to h"
    else: #lo que ocurre dentro del else si la condicion anterior no se cumple
        print "g is greater than h"