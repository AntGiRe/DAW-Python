"""Antonio Jesús Gil Reyes - Ejercicio 5"""

dic = {}
lis = [];

while True:
	#Menu
	print("\n1. Introduce nueva persona")
	print("2. Listar personas")
	print("3. Salir")
	opt = int(input("Introduce una opción: "))

	match opt:
		case 1:
			#Se pide un nombre y apellido. Se mete en el diccionario
			name = input("Introduce un nombre: ")
			lastname = input("Introduce un apellido: ")
			dic[name] = lastname
		case 2:
			#Sin terminar ordenacion
			print("Ordenar por:")
			print("1. Nombre")
			print("2. Apellido")
			opt = int(input("Introduce una opción: "))
		case 3:
			#Salir
			opt = input("¿Está seguro que desea salir (s/N)? ")
			if opt == "s":
				break
		case _:
			print("Se ha equivocado de opción")
