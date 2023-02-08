from e2 import Cuenta
from e1 import Persona

class CuentaJoven(Cuenta):

	"""Consutructor"""
	def __init__(self, titular, saldo, bonificacion):
		super().__init__(titular, saldo)
		self.bonificacion = bonificacion

	"""Setters & Getters"""
	@property
	def bonificacion(self):
		return self.__bonificacion

	@bonificacion.setter
	def bonificacion(self, bonificacion):
		if bonificacion > 0:
			self.__bonificacion = bonificacion
		else:
			self.__bonificacion = 0

	"""Función que comprueba si un titular es valido"""
	def esTitularValido(self):
		if self.titular.age < 25 and self.titular.esMayorDeEdad():
			return True
		else:
			return False

	"""Se retira si es un titular válido"""
	def retirar(self, cantidad):
		if self.esTitularValido():
			return super().retirar(cantidad)
		print("No se ha producido la retirada, titular no valido")

	def mostrar(self):
		print(" - - - - - - | CUENTA JOVEN | - - - - - -")
		super().mostrar()
		print("Bonificación: " + str(self.bonificacion) + "%")

if __name__ == '__main__':
	p1 = Persona("Pepe", 57, "56565656P")
	c1 = CuentaJoven(p1, 100, 10)

	c1.mostrar()
	c1.ingresar(100)
	c1.retirar(300)