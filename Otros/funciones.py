"""Funciones sin argumentos"""
print("\tFunciones sin argumentos")

def saluda():
	print("Hola");

saluda()

"""Funciones con argumentos"""
print("\tFunciones con argumentos")

def saluda(nombre, apellido):
	print("Hola", nombre, apellido);

saluda ("Juan", "Perez");

"""Argumentos por defecto"""
print("\tArgumentos por defecto")

def saluda(nombre = "Juan", apellido = "Perez"):
	print("Hola", nombre, apellido);

saluda("Pepe");
saluda(apellido = "Gerardo");

"""Argumentos variables"""
print("\tArgumentos variables")

def saluda(*nombres):
	for nombre in nombres:
		print("Hola", nombre);

saluda("Juan", "Pepe", "Maria");

"""Argumentos variables con clave"""
print("\tArgumentos variables con clave")

def saluda(**nombres):
	for nombre in nombres:
		print("Hola", nombre, nombres[nombre]);

saluda(Juan = "Perez", Pepe = "Gomez", Maria = "Lopez");

print(" - - - - - - - ")

def saluda(**nombres):
	for nombre, apellido in nombres.items():
		print("Hola", nombre, apellido);

saluda(Juan = "Perez", Pepe = "Gomez", Maria = "Lopez");

print(" - - - - - - - ")

def saluda (*saludos, **nombres):
	"""Argumentos variables y argumentos variables con clave"""
	for saludo in saludos:
		print(saludo);
	for nombre, apellido in nombres.items():
		print(nombre, apellido);

saluda("Hola", "Hello", "Bonjour", Juan = "Perez", Pepe = "Gomez", Maria = "Lopez");

print("\tCon help se puede ver la documentacion de la funcion")
help(saluda)

"""Funciones lambda"""
print("\tFunciones lambda")
suma = lambda a, b: a + b
print("Suma: ", suma(3,4))
cambia = lambda a, b: (b, a)
print("Cambia: ", cambia(3,4))

"""Funcion con argumento lambda"""
print("\tFuncion con argumento lambda")
def unafuncion(unalambda):
	return unalambda(3,4)

print("Suma: ", unafuncion(suma))

"""Funcion recursiva"""
print("\tFuncion recursiva")
def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

print("Factorial de 5: ", factorial(5))