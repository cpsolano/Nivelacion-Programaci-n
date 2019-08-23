a = ["banana", "apple", "microsoft"] #lista

for element in a: #para recorrer a
	print element #se imprime el elemento de la lista
	print element #se imprime de nuevo el elemento de la lista

b = [20,10,5] #lista
total = 0 #variable
for e in b: #se recorre
	total = total + e

print total #se imprime la nueva lista

c = list(range(1,5)) #se puede definir una variable como una lista
print c #se imprime c

total2 = 0 #se define variable
for i in range(1,5): #se recorre una lista [1,2,3,4]
	total2 += i 

print total2 #imprime total2

print(list(range(1,8)))

total3 = 0 #se define la variable

for i in range(1,8):
	if i%3==0: #para dejar el resto
		total3 += i

print total3 #imprime total3



