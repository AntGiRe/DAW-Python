"""Antonio Jesús Gil Reyes - Ejercicio 3"""

class Punto:
	# Constructor de la clase Punto
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	# Setters & Getters
	@property
	def x(self):
		return self.__x

	@property
	def y(self):
		return self.__y

	@x.setter
	def x(self,x):
		if (isinstance(x, int)):
			self.__x = x
		else:
			raise TypeError("x debe ser un numero entero")

	@y.setter
	def y(self,y):
		if (isinstance(y, int)):
			self.__y = y
		else:
			raise TypeError("y debe ser un numero entero")

	# Método que muestra el Punto
	def mostrar(self):
		print("(" + str(self.x) + "," + str(self.y) + ")");

	# Método que invierte las coordenadas
	def invierteCoordenadas(self):
		x_copy = self.x
		self.x = self.y
		self.y = x_copy

###########
# PRUEBAS #
###########

# He creado dos puntos, uno vacio y otro con x e y
p1 = Punto()
p2 = Punto(2,5)

# Muestro los Puntos
p1.mostrar()
p2.mostrar()

# Cambios los Puntos de p1
p1.x = 5
p1.y = 6
p1.mostrar()

# Invierto coordenadas
p1.invierteCoordenadas()
p1.mostrar()

# Intento meter valores incorrectos

try:
	p2 = Punto("e",5)
except TypeError as e:
	print(e)