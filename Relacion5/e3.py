#Antonio J. Gil ~ 19/10

def deletePerson(name):
	flag = 0

	f = open("agenda.txt","r")
	lines = f.readlines()
	f.close()

	w = open("agenda.txt","w")
	for line in lines:
		if(line[:line.index(";")] != name):
			w.write(line)
		else:
			flag += 1
	w.close()
	if (flag == 0):
		print("La persona introducida no existe.", end="\n\n")
	else:
		print("Persona eliminada correctamente.", end="\n\n")

def getPhone(name):
	f = open("agenda.txt","r")
	lines = f.readlines()
	f.close()

	for line in lines:
		if(name == line[:line.index(";")]):
			return(line[line.index(";") + 1:])
	return None

def addPerson(name, tlf):
	f = open('agenda.txt', 'a')
	f.write(name + ";" + tlf + "\n")
	f.close()
	print("Persona insertada correctamente.", end="\n\n")
	
def createAgenda():
	f = open('agenda.txt', 'a')
	f.close()
	print("Se ha creado/abierto el fichero", end="\n\n")

createAgenda()
while True:
	print("1. Añadir nueva persona")
	print("2. Eliminar una persona")
	print("3. Consulta el telefono de una persona")
	print("4. Salir")
	n = input("Introduce un numero: ")

	if n >= "1" and n < "4":
		nombre = input("Introduce un nombre: ")
		if(n == "1"):
			telefono = input("Introduce un telefono: ")
			addPerson(nombre, telefono)
		if(n == "2"):
			deletePerson(nombre)
		if(n == "3"):
			if(getPhone(nombre) != None):
				print("El numero de " + nombre + " es: " + getPhone(nombre))
			else:
				print("No existe esa persona", end="\n\n")
	elif (n == "4"):
		break
	else:
		print("Introduce un numero correcto.", end="\n\n")