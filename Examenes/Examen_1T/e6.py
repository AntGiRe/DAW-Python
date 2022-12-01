"""Antonio Jesús Gil Reyes - Ejercicio 6"""

import random

#Rellenamos un array de 6 filas por 7 columnas de manera aleatoria entre 0 y 100
numbers = []
aux = []
while len(numbers) < 6:
	number = random.randint(0, 100)
	aux.append(number);
	if(len(aux) == 7):
		numbers.append(aux);
		aux = [];

max = 0
min = 100

for row in range(len(numbers) + 1):
	if (row < len(numbers)):
		#Muestra cada fila y columna
		for col in range(len(numbers[0])):
			print(str(numbers[row][col]) + "\t|  ", end="");
			#Si el numero es mayor al maximo actual, se cambia
			if(numbers[row][col] > max):
				posMax = []
				max = numbers[row][col]
				posMax.append(row)
				posMax.append(col)
			#Si el numero es menor al minimo actual, se cambia
			if(numbers[row][col] < min):
				posMin = []
				min = numbers[row][col]
				posMin.append(row)
				posMin.append(col)
		print("")

#Mostramos el mayor y menor junto a sus coordenadas
print(posMax)
print("El mayor es " + str(max) + " [" + str(posMax[0]) + "," + str(posMax[1]) + "]");
print("El menor es " + str(min) + " [" + str(posMin[0]) + "," + str(posMin[1]) + "]");