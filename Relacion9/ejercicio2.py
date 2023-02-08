import ejercicio1
import sys

"""Descifra el texto con el metodo de Cesar. Devuelve el texto descifrado"""
def decodeCaesarCipher(texto, clave):
	cifrado = ""
	"""tener en cuenta solo caracteres alfabeticos"""
	for i in texto:
		cifrado += chr(ord(i) - clave)
	return cifrado

if __name__ == "__main__":
	try:
		type = ejercicio1.checkData()
		f = open(sys.argv[1], "r")
		texto = f.read()
		f.close()

		print("Introduzca la clave de cifrado. En positivo, valores a la derecha. En negativo, valores a la izquierda")
		clave = int(input())

		if type == 1:
			f = open(sys.argv[1], "w")
		else:
			f = open(sys.argv[2], "w")
		f.write(decodeCaesarCipher(texto, clave))
		f.close()
		
	except IOError:
		print("Error: No se puede leer el archivo")
		sys.exit(2)
