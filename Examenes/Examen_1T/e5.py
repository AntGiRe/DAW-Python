"""Antonio Jesús Gil Reyes - Ejercicio 5"""

mi_dict = {}

while True:
	#Menu
	print("\n1. Introduce nueva persona")
	print("2. Listar personas por nombre")
	print("3. Listar personas por apellidos")
	print("4. Salir")
	opt = int(input("Introduce una opción: "))

	match opt:
		case 1:
			#Se pide un nombre y apellido. Se mete en el diccionario
			name = input("Introduce un nombre: ")
			lastname = input("Introduce un apellido: ")
			mi_dict[name] = lastname
		case 2:
			mi_list = list(mi_dict.keys())
			mi_dict_aux = {}
			mi_list.sort()
			for nombre in mi_list:
				mi_dict_aux[nombre] = mi_dict[nombre]
			mi_dict = mi_dict_aux
			print("El diccionario ordenado es: ", mi_dict)
		case 3:
			mi_lista_apellidos = list(mi_dict.values())
			mi_lista_nombres = list(mi_dict.keys())
			mi_lista_apellidos.sort()
			mi_dict_aux = {}
			for apellido in mi_lista_apellidos:
				for nombre in mi_lista_nombres:
					if mi_dict[nombre] == apellido:
						mi_dict_aux[nombre] = apellido
			mi_dict = mi_dict_aux
			print("El diccionario ordenado es: ", mi_dict)
		case 4:
			#Salir
			opt = input("¿Está seguro que desea salir (s/N)? ")
			if opt == "s":
				break
		case _:
			print("Se ha equivocado de opción")
