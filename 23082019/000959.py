given_list2 = [5,4,4,3,1,-2,-3,-5] #se genera lista
total5 = 0 #variable
i = 0 #variable contador
while True: #se pone condicion que siempre es verdad
    total5 += given_list2[i] #se le suman los valores de la lista uno por uno a la variable
    i += 1 #se le suma 1 al contador
    if given_list2[i] <= 0: #condicion para poder cortar el loop
        break #corta el loop
print total5 #se imprime la variable
