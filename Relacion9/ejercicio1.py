import sys

"""Devuelve 1 si solo hay un argumento, 2 si hay dos. En otro caso, error"""
def checkData():
	if(len(sys.argv) < 2 or len(sys.argv) > 3):
		print("Error: Numero de argumentos incorrecto")
		sys.exit(1)
	elif(len(sys.argv) == 2):
		print("Se machará el archivo " + sys.argv[1] + ", ¿desea continuar? (s/n)")
		respuesta = input()
		if(respuesta == "s"):
			return 1
		else:
			sys.exit(3)
	else:
		return 2

"""Cifra el texto con el metodo de Cesar. Devuelve el texto cifrado"""
def CaesarCipher(texto, clave):
	cifrado = ""
	for i in texto:
		cifrado += chr(ord(i) + clave)
	return cifrado

"""Programa principal"""
if __name__ == "__main__":
	try:
		type = checkData()
		f = open(sys.argv[1], "r")
		texto = f.read()
		f.close()

		print("Introduce la clave. En positivo, valores a la izquierda. En negativo, valores a la derecha")
		clave = int(input())

		if type == 1:
			f = open(sys.argv[1], "w")
		else:
			f = open(sys.argv[2], "w")
		f.write(CaesarCipher(texto, clave))
		f.close()

	except IOError:
		print("Error: No se puede escribir en el archivo")
		sys.exit(2)