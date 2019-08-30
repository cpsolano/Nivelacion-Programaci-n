from matplotlib import pyplot as plt
import numpy as np

ages_x = range(25,36) #lista

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640] #lista

plt.plot(ages_x, py_dev_y, color = "#5a7d9a", linewidth = 3 , label = "Python") #se crea grafico con ages_x en eje x y py_dev_y en eje y
#color define el color en que se va a mostrar la linea, linewidth permite hacer mas delgada o gruesa la linea

js_dev_y =  [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583] #lista

plt.plot(ages_x, js_dev_y, color = "#adad3b",linewidth = 3 ,label = "JavaScript")#se crea grafico con ages_x en eje x y js_dev_y en eje y
#color define el color en que se va a mostrar la linea, linewidth permite hacer mas delgada o gruesa la linea

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752] #lista
#label en los plt.plt permite identificar lo que se plotea con un nombre

plt.plot(ages_x, dev_y, color = "#444444", linestyle ="--", marker = "o", label = "All Devs") #se crea grafico con ages_x en eje x y dev_y en eje y
#linestyle permite definir como se mostrara la linea (en este caso punteada), marker permite poner algo distintivo en los puntos graficados, en este caso un circulo
plt.xlabel("Ages") #nombre al eje x
plt.ylabel("Median Salary (USD)") #nombre al eje Y
plt.title("Median Salary (USD) by Age") #titulo grafico

plt.legend()#para agregar leyenda en el grafico

plt.grid(True) #para poner malla en el grafico

plt.tight_layout() #ajusta el grafico

plt.show() #para mostrar el grafico
