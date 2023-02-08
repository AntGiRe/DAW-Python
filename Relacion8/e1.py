class Persona:
	"""Constructor"""
	def __init__(self, name="Sin nombre", age=0, dni="00000000A"):
		self.name = name
		self.age = age
		self.dni = dni

	"""Función que comprueba si es mayor de edad una persona"""
	def esMayorDeEdad(self):
		if self.age >= 18:
			return 1
		else:
			return 0
	
	"""Muestra informacion de persona"""
	def mostrar(self):
		print(" - - / " + self.name + " \ - -")
		print("Tiene el siguiente DNI: " + self.dni)
		print("Tiene " + str(self.age) + " años, por lo que es", end="");
		if self.esMayorDeEdad():
			print(" mayor ", end="");
		else:
			print(" menor ", end="")
		print("de edad.")

	"""Setters & getters"""
	@property 
	def name(self):
		return self.__name

	@property 
	def age(self):
		return self.__age

	@property 
	def dni(self):
		return self.__dni

	@age.setter
	def age(self, new_age):
		if new_age >= 0:
			self.__age = new_age
			return True
		else:
			return False

	@name.setter
	def name(self, new_name):
		if len(new_name) > 0:
			self.__name = new_name
			return True
		else:
			return False

	@dni.setter
	def dni(self, new_dni):
		codDNI='TRWAGMYFPDXBNJZSQVHLCKE'
		if len(new_dni) == 9:
			if new_dni[:-1].isnumeric():
				letraDni = int(new_dni[:-1])%23;
				if(new_dni[-1].upper() == codDNI[letraDni]):
					self.__dni = new_dni
					return True
		self.__dni = "No válido"
		return False

if __name__ == '__main__':
	"""Creamos una persona e imprimos su información"""
	an = Persona("Antonio", 20, "2626f82s")

	print(an.dni)

	an.mostrar()


