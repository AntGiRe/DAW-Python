"""Antonio J Gil 	-	11/11"""

"""Esta función devuelve en una lista como clave el billete y como valor el numero de billetes necesarias hasta llegar a una cantidad con los menores billetes posibles"""
def moneyDesco(money):
	bills = [100,50,20,10,5];
	arrayBills = {};

	#Se va revisando si la division da igual o mas de 1, en ese caso guardamos division en array y nos quedamos con el resto. Asi descendiendo hasta el 1
	for bill in bills:
		if money / bill >= 1:
			arrayBills[bill] = money // bill;
			money = money % bill;
	return(arrayBills);

"""Esta función muestra el diccionario con los billetes y el numero de billetes"""
def showMoney(arrayBills):
	for bill in arrayBills:
		nbrBills = arrayBills[bill];
		print("Necesitamos " + str(nbrBills) + " de billetes de " + str(bill));

while True:
	try:
		money = int(input("Dinero a retirar: "));
		if (money < 0):
			print("No puede retirar una cantidad negativa");
		elif (money % 5 != 0):
			print("Lo sentimos no devolvemos monedas, solo divisores de 5");
		else:
			showMoney(moneyDesco(money));
			break;
	except ValueError:
		print("Valor erroneo");