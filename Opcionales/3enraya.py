from random import randrange

#Muestra el tablero
def showTab(tab, player, machine):
	print("-------------")
	for k in tab:
		print("|", end = " ")
		for j in k:
			if (j == 1):
				print(player, end=" | ")
			elif (j == 2):
				print(machine, end= " | ")
			else:
				print(end="  | ")
		print("")
		print("-------------")

#Movimiento del jugador
def playerMove(tab, x, y):
	if (tab[x][y] == 0):
		tab[x][y] = 1
		return(tab)
	else:
		return(None)

#Movimiento de la maquina
def MachineMove(tab):
	while(True):
		row = randrange(0, 3)
		col = randrange(0, 3)
		if (tab[row][col] == 0):
			tab[row][col] = 2
			return(tab)

#Comrpueba si la maquina es ganadora
def checkMachine(tab):
	count = 0
	#Comprueba verticalmente de la maquina
	for k in tab:
		for j in k:
			if(j == 2):
				count += 1
			else:
				count = 0
				break;
		if (count == 3):
			return(True)
		else:
			count = 0

	#Comprueba horizontalmente de la maquina
	for k in range(3):
		if(tab[0][k] == tab[1][k] == tab[2][k] == 2):
			return(True)

	#Comprueba las diagonales de la maquina
	if(tab[0][0] == tab[1][1] == tab[2][2] == 2):
		return(True)
	elif(tab[0][2] == tab[1][1] == tab[2][0] == 2):
		return(True)

#Comprueba si el jugador es ganador
def checkPlayer(tab):
	count = 0
	#Comprueba verticalmente del jugador
	for k in tab:
		for j in k:
			if(j == 1):
				count += 1
			else:
				count = 0
				break;
		if (count == 3):
			return(True)
		else:
			count = 0

	#Comprueba horizontalmente del jugador
	for k in range(3):
		if(tab[0][k] == tab[1][k] == tab[2][k] == 1):
			return(True)

	#Comprueba las diagonales del jugador
	if(tab[0][0] == tab[1][1] == tab[2][2] == 1):
		return(True)
	elif(tab[0][2] == tab[1][1] == tab[2][0] == 1):
		return(True)

#Comprueba cuantos huecos libres quedan en el tablero
def checkEmpty(tab):
	count = 0
	for k in tab:
		for j in k:
			if(j == 0):
				count += 1
	return(count)

#Crea archivo si no existe
def createRanking():
	file = open("ranking.txt", "a")
	file.close()

#Actualiza ranking
def updateRanking(username):
	flag = 0
	file = open("ranking.txt","r")
	lines = file.readlines()
	file.close()

	w = open("ranking.txt", "w")
	for line in lines:
		if(line[:line.index(";")] != username):
			w.write(line)
		else:
			w.write(username + ";" + str(int(line[line.index(";") + 1:]) + 1) + "\n")
			flag = 1
	if(len(lines) == 0 or flag == 0):
		w.write(username + ";1" + "\n")
	w.close()

#Muestra ganadores de 3raya
def showRanking():
	f = open("ranking.txt", "r")
	lines = f.readlines()
	f.close()

	for line in lines:
		print(line[:line.index(";")] + " - " + line[line.index(";") + 1 : line.index("\n")] + " victorias")

#Se crea el archivo ranking si no existe
createRanking()

tab = [[0 for k in range(3)] for j in range(3)]
player = "vacio"
end = False

username = input("Introduce el nombre de usuario: ")

#El jugador elige su caracter
while(len(player) > 1):
	player = input("Elige un caracter con el que jugar: ")

#La maquina elige su caracter
if (player != 'O'):
	machine = 'O'
else:
	machine = 'X'

print("\n¡Decidido!")
print("Tú serás " + player)
print("Y yo " + machine)
print("Ten en cuenta que las filas y columnas empiezan en 0 hasta el 2")
print("¡¡Te ganaré miserable humano!!\n")

while(end != True):
	showTab(tab, player, machine)
	#Si la maquina gana o no quedan huecos se acaba. Si no, se sigue
	if(checkMachine(tab)):
		end = True
		print("¡La maquina gana!")
	elif(checkEmpty(tab) == 0):
		print("Se acabaron los huecos libres")
		end = True
	else:
		while (True):
			#Se revisan si lo introducido es correcto
			while (True):
				try:
					x = int(input("Introduce numero de fila: "))
					y = int(input("Introduce numero de columna: "))
					newTab = playerMove(tab, x, y)
					break;
				except ValueError:
					print("Has introducido valores erroneos, intentalo de nuevo")
				except IndexError:
					print("Te has pasado de largo, revisa los numeros")
					print("¡Ten en cuenta que las filas y columnas empiezan en 0 hasta el 2!")
					showTab(tab, player, machine)
			if (newTab != None):
				tab = newTab
				break;
		#Si el jugador gana o no quedan huecos, se acaba. Si no, se sigue.
		if(checkPlayer(tab)):
			end = True
			print("¡El jugador gana!")
			#Suma una victoria en el ranking
			updateRanking(username)
		elif(checkEmpty(tab) == 0):
			print("Se acabaron los huecos libres")
			end = True
		else:
	 		tab = MachineMove(tab)

showTab(tab, player, machine)
print("\nTodos los demás ganadores:")
showRanking()