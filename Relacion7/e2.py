#Antonio Gil :D
"""Funcion que calcula el precio total de los articulos, pasando como parametro el numero de articulos a comprar"""
def calculaPrecios(num, **articulos):
	suma = 0
	print("\tArticulos:")
	print("COMPRADOS:", num, " objetos de cada")
	for articulo in articulos:
		precio = articulos[articulo]*num;
		print(articulo, " - ", articulos[articulo], "€/u:   ", precio, "€")
		suma += precio;
	print("La suma total es de:", suma)

calculaPrecios(4, ChupaChups = 0.40, Compresas = 5, Lapices = 1, Boligrafo = 1)