#Antonio J. Gil ~ 19/10
class Persona():
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def get_nombre(self):
		return self.nombre

	def get_edad(self):
		return self.edad

	def set_edad(self, edad):
		self.edad = edad

	def set_nombre(self, nombre):
		self.nombre = nombre
	
	def print_persona(self):
		print("El nombre es: " + self.nombre + " y la edad es: " + str(self.edad))
	
	def es_mayor_de_edad(self):
		return True if self.edad >= 18 else False

	def es_mayor_que(self, persona):
		if (persona.get_edad() < self.edad):
			return "Tu eres mayor que esa persona"
		elif ( self.edad < persona.get_edad()):
			return "Esa persona es mayor que tu"
		else:
			return "Teneis la misma edad"
	
	@staticmethod
	def get_mayor(persona1, persona2):
		if (persona1.get_edad() > persona2.get_edad()):
			return persona1
		elif (persona2.get_edad() > persona1.get_edad()):
			return persona2
		else:
			return None


a = Persona("Antonio", 20)
b = Persona("Amalia", 13)

a.print_persona()
b.print_persona()

print("Antonio", a.es_mayor_de_edad())
print("Amalia", b.es_mayor_de_edad())

print(a.es_mayor_que(b), "Antonio")
print(b.es_mayor_que(a), "Amalia")

print("El mayor es la siguiente persona:");
p = Persona.get_mayor(a, b)
p.print_persona()
