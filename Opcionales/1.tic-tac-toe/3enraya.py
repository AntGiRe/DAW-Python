"""Antonio J. Gil Reyes || 24/10/22"""

from random import randrange

#Show the board of the game
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

#The player moves
def playerMove(tab, x, y):
	if (tab[x][y] == 0):
		tab[x][y] = 1
		return(tab)
	else:
		return(None)

#The machine moves
def machineMove(tab):
	while(True):
		row = randrange(0, 3)
		col = randrange(0, 3)
		if (tab[row][col] == 0):
			tab[row][col] = 2
			return(tab)

#Check if the machine wins
def checkMachine(tab):
	count = 0
	#Check vertically
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

	#Check horizontally
	for k in range(3):
		if(tab[0][k] == tab[1][k] == tab[2][k] == 2):
			return(True)

	#Check diagonally
	if(tab[0][0] == tab[1][1] == tab[2][2] == 2):
		return(True)
	elif(tab[0][2] == tab[1][1] == tab[2][0] == 2):
		return(True)

#Check if the player wins
def checkPlayer(tab):
	count = 0
	#Check vertically
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

	#Check horizontally
	for k in range(3):
		if(tab[0][k] == tab[1][k] == tab[2][k] == 1):
			return(True)

	#Check diagonally
	if(tab[0][0] == tab[1][1] == tab[2][2] == 1):
		return(True)
	elif(tab[0][2] == tab[1][1] == tab[2][0] == 1):
		return(True)

#Return number of empty holes
def checkEmpty(tab):
	count = 0
	for k in tab:
		for j in k:
			if(j == 0):
				count += 1
	return(count)

#Create the ranking file
def createRanking():
	file = open("ranking.txt", "a")
	file.close()

#Update the ranking file
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

#Show the ranking of the game
def showRanking():
	f = open("ranking.txt", "r")
	lines = f.readlines()
	f.close()

	for line in lines:
		print(line[:line.index(";")] + " - " + line[line.index(";") + 1 : line.index("\n")] + " victorias")

createRanking()

tab = [[0 for k in range(3)] for j in range(3)]
player = "vacio"
end = False

username = input("Introduce el nombre de usuario: ")

#The player chooses his token
while(len(player) > 1):
	player = input("Elige un caracter con el que jugar: ")

#The machine chooses his token too
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
	#If the machine wins or not empty holes left, game ends. If not, show must go on
	if(checkMachine(tab)):
		end = True
		print("¡La maquina gana!")
	elif(checkEmpty(tab) == 0):
		print("Se acabaron los huecos libres")
		end = True
	else:
		while (True):
			#Check if input is OK
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
		#If player wins or not empty holes left, game ends. If not, show must go on.
		if(checkPlayer(tab)):
			end = True
			print("¡El jugador gana!")
			updateRanking(username)
		elif(checkEmpty(tab) == 0):
			print("Se acabaron los huecos libres")
			end = True
		else:
	 		tab = machineMove(tab)

showTab(tab, player, machine)
print("\nTodos los demás ganadores:")
showRanking()