from matplotlib import pyplot as plt
import numpy as np
plt.style.use("fivethirtyeight") #estilo provisto por matplotlib para un grafico
#plt.style.use("ggplt")

ages_x = range(25,36) #lista

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640] #lista

plt.plot(ages_x, py_dev_y, label = "Python") #se crea grafico con ages_x en eje x y py_dev_y en eje y

js_dev_y =  [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583] #lista

plt.plot(ages_x, js_dev_y,label = "JavaScript") #se crea grafico con etiqueta asociada

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752] #lista
#label en los plt.plt permite identificar lo que se plotea con un nombre

plt.plot(ages_x, dev_y, color = "#444444", linestyle ="--", label = "All Devs") #se crea grafico con ages_x en eje x y dev_y en eje y
#color permite definir el color de la linea que grafica, linestyle permite definir como se mostrara la linea (en este caso punteada)
plt.xlabel("Ages") #nombre al eje x
plt.ylabel("Median Salary (USD)") #nombre al eje Y
plt.title("Median Salary (USD) by Age") #titulo grafico

plt.legend()#para agregar leyenda en el grafico

plt.tight_layout() #ajusta el grafico
plt.savefig("plot.png") #guarda la imagen en la carpeta donde se encuentra con el nombre escrito en el parentesis
plt.show() #para mostrar el grafico