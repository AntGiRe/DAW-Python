"""Antonio Jesús Gil Reyes - Ejercicio 4"""

# Funcion que abre un fichero y comprueba posibles excepciones
def openFile(tipe):
	try:
		return open("listaCompra.txt", tipe)
	except IOError:
		print("Error: No se puede leer el archivo")

# Funcion que crea un articulo en un fichero
def createArt(art):
	f = openFile("a")
	if f:
		f.write(art + "\n")
		f.close()
		print("Articulo añadido correctamente")

# Funcion que borra un articulo en un fichero
def deleteArt(art):
	f = openFile("r")
	if f:
		text = f.read()
		f.close()

		if (text.find(art) < 0):
			print("El artículo introducido no existe")
		else:
			text = text.replace(art + "\n", "")

			f = openFile("w")
			if f:
				f.write(text)
				f.close()

				print("El artículo ha sido eliminado correctamente")

# Menú
while True:
	print(" 1. Crear/Añadir Artículo")
	print(" 2. Borrar Artículo")
	print(" 3. Salir")

	# Comprueba ValueError en caso de no introducir un numero
	try:
		option = int(input("Introduce una opción: "))

		if option == 1:
			art = input("Introduce el artículo: ")
			createArt(art)
		elif option == 2:
			art = input("Introduce el artículo: ")
			deleteArt(art)
		elif option == 3:
			break
		else:
			print("Opción incorrecta, vuelve a intentarlo")
	except ValueError:
		print("Has introducido un numero erróneo")