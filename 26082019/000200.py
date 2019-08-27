d = {} #se crea un diccionario vacio
d["George"] = 24 #se genera un valor (24) enlazado a la variable "George"
d["Tom"] = 32 #se genera un valor (32) enlazado a la variable "Tom"
d["Jenny"] = 16 #se genera un valor (16) enlazado a la variable "Jenny"
print d["George"] # se imprime el valor asociado a George

d["Jenny"] = 20 #se cambia el valor asociado a "Jenny" de 16 a 20

print d["Jenny"] #se imprime el valor nuevo de "Jenny"

d[10] = 100 #se genera el valor 100 asociado a 10

print d[10] #se imprime el valor asociado a 10 (100)

for key, value in d.items(): #como iterar sobre pares de llave-valor
    print "Key:" #Se imprime esto textual
    print key #se imprime el indice del diccionario (ej: George, Jenny)
    print "Value:" #Se imprime esto textual
    print value #se imprime el valor asociado a cada indice impreso arriba
    print "" #Para dar un espacio entre cada iteracion
