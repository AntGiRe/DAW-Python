#Antonio J. Gil ~ 19/10
class NumberNotValid(Exception):
	def __init__(self):
		pass
	
	def __str__(self):
		return f'Has introducido un numero no valido'

try:
	n = int(input("Introduce un numero del 1 al 10: "))
	if n < 1 or n > 10:
		raise NumberNotValid
	f = open('tabla-' + str(n) + '.txt', 'w')
	for i in range(1, 11):
		f.write(str(n) + " x " + str(i) + " = " + str(n*i) + "\n")
	f.close()
except NumberNotValid as err:
	print(err)