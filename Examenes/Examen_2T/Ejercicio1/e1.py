"""Antonio Jesús Gil Reyes - Ejercicio 1"""

# Función lambda que realiza la suma de dos variables
suma = lambda n1, n2: n1 + n2

def checkInt(nbr, err):
	if (isinstance(nbr, int)):
		return True
	else:
		raise TypeError(err)

# Función que mezcla dos listas
def mezcla(a, b):
	i = 0
	lista = []
	while True:
		i += 1
		if len(a) >= i and checkInt(a[i - 1], "Hay un caracter no numerico en la lista A"):
			lista.append(a[i - 1])
		if len(b) >= i and checkInt(b[i - 1], "Hay un caracter no numerico en la lista B"):
			lista.append(b[i - 1])
		if (suma(len(b), len(a)) == len(lista)):
			break
	return lista

###########
# PRUEBAS #
###########

print("1,2 --- 7,8,9,10")
print (mezcla([1,2],[7,8,9,10]))

print("\n --- 7,8,9,10")
print (mezcla([],[7,8,9,10]))

print("\n1,2,4,7 --- 7,8,9,10")
print (mezcla([1,2,4,7],[7,8,9,10]))

print("\n1,e,4,7 --- 7,8,9,10")
try:
	print (mezcla([1,"e",4,7],[7,8,9,10]))
except TypeError as e:
	print(e)