#Antonio Gil :D
"""Funcion que muestra los numeros mayores y menores de una lista a partir de un numero pasado como parametro"""
def devuelveMenMay(num, *numeros):
	menores = []
	mayores = []
	print("El numero de corte fue:", num)
	for n in numeros:
		if n > num:
			menores.append(n)
		elif num > n:
			mayores.append(n)
	print("Mayor: ", mayores)
	print("Menor: ", menores)

devuelveMenMay(10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)