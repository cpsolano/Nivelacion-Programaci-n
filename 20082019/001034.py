# BMI calculator
name1 = "YK" #variable
height_m1 = 2 #variable
weight_kg1 = 90 #variable

name2 = "YK's sister" #variable
height_m2 = 1.8 #variable
weight_kg2 = 70 #variable

name3 = "YK's brother" #variable
height_m3 = 2.5 #variable
weight_kg3 = 160 #variable

def bmi_calculator(name, height_m, weight_kg): #se define funcion dependiente de 3 variables
    bmi = weight_kg / (height_m**2) #se define variable dentro de la funcion
    print "bmi:" #Se imprime "bmi: "
    print bmi # se imprime la variable
    if bmi < 25: #Se crea condicion
        return name + " is not overweight" #se guarda la informacion en caso de cumplirse la condicion
    else: # se recurre a esta condicion en caso de que no se cumpla lo anterior
        return name + " is overweight" #se guarda la informacion en caso de cumplirse la condicion else

result1 = bmi_calculator(name1, height_m1, weight_kg1) #variable para guardar la informacion de la funcion
result2 = bmi_calculator(name2, height_m2, weight_kg2) #variable para guardar la informacion de la funcion
result3 = bmi_calculator(name3, height_m3, weight_kg3) #variable para guardar la informacion de la funcion

print result1 # imprime lo de la variable
print result2 # imprime lo de la variable
print result3 # imprime lo de la variable
