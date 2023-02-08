from e1 import Persona

class Cuenta:

	"""Consutructor"""
	def __init__(self, titular, saldo=0):
		self.titular = titular
		self.__saldo = saldo

	"""Setters & Getters"""
	@property
	def saldo(self):
		return self.__saldo

	@saldo.setter
	def saldo(self):
		pass

	@property
	def titular(self):
		return self.__titular

	@titular.setter
	def titular(self, titular):
		self.__titular = titular
	
	"""Función que ingresa una cantidad a la cuenta"""
	def ingresar(self, cantidad):
		if cantidad > 0:
			print("Se ha producido el ingreso")
			self.__saldo += cantidad
		else:
			return False

	"""Función que retira una cantidad de la cuenta"""
	def retirar(self, cantidad):
		if cantidad > 0:
			print("Se ha producido la retirada")
			self.__saldo -= cantidad
		else:
			return False
	
	"""Muestra la información de la cuenta"""
	def mostrar(self):
		print(" - - / " + self.titular.name + " \ - -")
		print("Tiene un saldo de " + str(self.saldo) + "€")

if __name__ == '__main__':
	"""Creamos una persona y cuenta. Ingresamos y retiramos dinero"""
	an = Persona("Er Paco", 15, "3432s")

	c = Cuenta(an, 5)

	c.ingresar(100)

	c.retirar(200)

	c.mostrar()