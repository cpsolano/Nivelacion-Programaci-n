given_list = [5,4,4,3,1] #se genera lista de valores positivos

total3 = 0 #variable
i = 0 #variable que se usara como contador

while i < len(given_list) and given_list[i] > 0: #se pone doble condicion para entrar al loop
    total3 += given_list[i] #se suman los valores de la lista a la variable
    i += 1 #se le suma 1 al contador

print total3 #se imprime la variable
