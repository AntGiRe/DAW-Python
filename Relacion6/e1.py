"""Antonio J Gil 	-	11/11"""

"""Creamos una matrix de 4 filas y 5 columnas, controlando la entrada, sin permitir otros caracteres distintos de los numericos"""
def createMatrix4Rows5Cols():
	numbers = []
	aux = []
	while len(numbers) < 4:
		try:
			number = int(input("Introduce numero: "));
			aux.append(number);
			if(len(aux) == 5):
				numbers.append(aux);
				aux = [];
		except ValueError:
			print("Valor erroneo");
	return numbers;

"""Imprime una tabla de 4 filas y 5 columnas a partir de una matrix. Ademas muestra suma de filas y columnas y la suma total"""
def printTable4Rows5Cols(numbers):
	sumY = [];
	#Cabecera de la tabla
	print("\t C1\t C2\t C3\t C4\t C5\t\tTotal")
	for row in range(len(numbers) + 1):
		sumX = 0;
		if (row < len(numbers)):
			#Muestra cada fila
			print("F" + str(row+1) +"\t",end="");
			for col in range(len(numbers[0])):
				if (row == 0):
					sumY.append(numbers[row][col]);
				else:
					sumY[col] += numbers[row][col];
				sumX += numbers[row][col];
				print(str(numbers[row][col]) + "\t|  ", end="");
		else:
			#Muestra la suma de las columnas
			print("\nTotal\t",end="");
			for col in range(len(numbers[0])):
				sumX += sumY[col];
				print(str(sumY[col]) + "\t| ", end="");
		#Muestra la suma de todas las filas
		print("\t" + str(sumX));

printTable4Rows5Cols(createMatrix4Rows5Cols());