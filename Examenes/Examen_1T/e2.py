"""Antonio Jesús Gil Reyes - Ejercicio 2"""
nbr = int(input("Introduce un numero: "))

#Si el resultado de la division entre 2 es cero, entonces es multiplo seguro.
if nbr % 2 == 0:
	cp = nbr
	#Se divide el numero hasta llegar a 2 o numero menor a 2
	while cp > 2:
		cp = cp / 2
	#Si el numero al que llegamos es 2, es potencia. Si no, no lo es.
	if cp == 2:
		print(str(nbr) + " es multiplo de 2 y potencia de 2")
	else:
		print(str(nbr) + " es multiplo de 2, pero no potencia de 2")
else:
	print(str(nbr) + " no es múltiplo de 2 ni potencia de 2")