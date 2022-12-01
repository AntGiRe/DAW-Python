"""Antonio Jesús Gil Reyes - Ejercicio 4"""

import random

#Genera una contraseña
passw = str(random.randint(1000, 9999))

while True:
	good = 0
	notbad = 0
	lis = []
	lis_good = []

	user = input("Introduce un numero: ")
	print(passw)

	#Si ha introducido la misma contraseña, ha ganado
	if(user == passw):
		print("Felicidades, lo has logrado :D")
		break
	else:
		#Se guarda en una lista todos los numeros de la contraseña y los numeros correctos
		for i in range(0,4):
			lis.append(passw[i])
			if(passw[i] == user[i]):
				good += 1
				lis_good.append(passw[i])
		
		#Se saca numeros que estan mal colocados
		for i in user:
			if i in lis:
				notbad += lis.count(i) - lis_good.count(i)
				
	print ("Tienes " + str(good) + " bien colocado/s")
	print ("Tienes " + str(notbad) + " mal colocado/s")