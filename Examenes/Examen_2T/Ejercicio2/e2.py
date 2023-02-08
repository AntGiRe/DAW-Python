"""Antonio Jesús Gil Reyes - Ejercicio 2"""

# Funcion que ordena de menor a mayor una lista numerica
def ordenaLista(lista):
	if (len(lista) <= 1):
		return lista
	else:
		if isSorted(lista):
			return lista
		else:
			big = max(lista)
			lista.remove(big)
			return ordenaLista(lista) + [big]

# Funcion que comprueba si la lista esta ordenada
def isSorted(lista):
	for nbr in lista:
		if (nbr < nbr + 1):
			return False
	return True
		

###########
# PRUEBAS #
###########

print(ordenaLista([1]))

print(ordenaLista([]))

print(ordenaLista([4,2,3]))

print(ordenaLista([4,2,3,7,4,657,32,456,34,1234,567,768,435,234,345,768]))

print(ordenaLista([54,56,23,78,12,89,89,34,2,34,23,89]))