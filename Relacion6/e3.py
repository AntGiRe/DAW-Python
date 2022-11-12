"""Antonio J Gil 	-	11/11"""
from random import randrange

"""La maquina de manera aleatoria elige 0, 1 o 2. En ese orden: piedra, papel o tijera"""
def machinePlay():
	machineSays = randrange(3);
	if (machineSays == 0):
		print("La maquina saca: PIEDRA");
	elif (machineSays == 1):
		print("La maquina saca: PAPEL");
	else:
		print("La maquina saca: TIJERA");
	return (machineSays);

"""El jugador escribe piedra, papel o tijera y esto es transformado en ese orden en 0, 1 o 2"""
def playerPlay(playerSays):
	if (playerSays == "PIEDRA"):
		print("El jugador saca: PIEDRA");
		return (0);
	elif (playerSays == "PAPEL"):
		print("El jugador saca: PAPEL");
		return (1);
	else:
		print("El jugador saca: TIJERA");
		return(2);

"""Devuelve 0 si hubo empate, devuelve 1 si gana la maquina y devuelve 2 si gana jugador"""
def game(playerSays):
	player = playerPlay(playerSays);
	machine = machinePlay();

	if(machine == player):
		return (0);
	elif((machine == 0 and player == 2) or (machine == 2 and player == 1) or (machine == 1 and player == 0)):
		return (1);
	return (2);

nbrTies = 0;
machineWins = 0;
playerWins = 0;
while True:
	playerSays = input("¿Piedra, papel o tijera? ").upper();
	if playerSays == "PIEDRA" or playerSays == "PAPEL" or playerSays == "TIJERA":
		result = game(playerSays);
		if (result == 0):
			print("¡Ha ocurrido un empate!");
			nbrTies += 1;
		elif (result == 1):
			print("¡La maquina gana!");
			machineWins += 1;
		else:
			print("¡El jugador gana!");
			playerWins += 1;
	else:
		machinePlay();
		machineWins += 1;
		print("¡Has perdido! Te has liado y no has sacado :c");
	if(input("\n¿Quieres volver a jugar?(Y/n)") == 'n'):
		print("Numero de victorias: " + str(playerWins) + "\nNumero de derrotas: " + str(machineWins) + "\nNumero de empates: " + str(nbrTies));
		break;