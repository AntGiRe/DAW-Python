""" USANDO TRY & EXCEPT CON EXCEPCIONES YA EXISTENTES EN PHYTON """

num1 = 3
try:
	num2 = "a"
except NameError as err:
	print("Has introducido algo raro, revisalo anda")

try:
	x = num1 / num2
except ZeroDivisionError as err:
	print("Perdone amigo, tiene un pequeño fallo, no puede dividir por cero. Le adjunto el error aqui en ingles:", err)
except TypeError as err:
	print("Los tipos no corresponde, cucha como vas a dividir un numero y un caracter. La juventud de hoy en dia...")
except Exception as err:
	print("Ha tenido usted un error raro, el codigo en ingles es:", err)

""" ERROR PERSONALIZADO """
class MyError(Exception):
	pass

try:
	raise MyError("De aqui no pasas, que te crees mu listo")
except MyError as err:
	print(err)

class SmallException(Exception):
	pass

class LargeException(Exception):
	pass

x = 22
while True:
	try:
		n = int(input("Intente adivinar mi numero:"))
		if n < x:
			raise SmallException
		elif n > x:
			raise LargeException
		break
	except SmallException:
		print("Te has quedado corto")
	except LargeException:
		print("Te has pasao")
print("Eres hiper inteligente, que crack. Has ganado el premio especial de esta noche: 10.000$ te esperan, solo rellena el formulario aquí")

class Err(Exception):
	def __init__(self, edad, mensaje):
		self.edad = edad
		self.msg = mensaje
	
	def __str__(self):
		return f'{self.edad} -> {self.msg}'

edad = int(input("Introduzca su edad: "))
mensaje = "Has introducido un valor erroneo"

try:
	if not 20 < edad < 50:
		raise Err(edad, mensaje)
	else:
		print("La edad es correcta")
except Err as err:
	print(err)