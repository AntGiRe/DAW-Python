import ejercicio1
import ejercicio2
import sys

"""Muestra todas las posbilidades de codigo cesar"""
def allmsg(texto):
	for i in range(1, 26):
		print("Clave: " + str(i) + " - Mensaje: " + ejercicio2.decodeCaesarCipher(texto, i))
	for i in range(-26, 0):
		print("Clave: " + str(i) + " - Mensaje: " + ejercicio2.decodeCaesarCipher(texto, i))

try:
	type = ejercicio1.checkData()
	f = open(sys.argv[1], "r")
	texto = f.read()
	f.close()

	print("Elige el mensaje: ")
	allmsg(texto)
	clave = int(input())

	if type == 1:
		f = open(sys.argv[1], "w")
	else:
		f = open(sys.argv[2], "w")
	f.write(ejercicio2.decodeCaesarCipher(texto, clave))
	f.close()
except IOError:
	print("Error: No se puede leer el archivo")
	sys.exit(2)