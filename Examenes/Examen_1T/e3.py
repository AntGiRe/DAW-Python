"""Antonio Jesús Gil Reyes - Ejercicio 3"""

#Se pide la cadena por pantalla y la cortamos en palabras
str = input("Introduce un texto: ");
list = str.split();

dic = {};

#Se recorren todas las palabras de la cadena
for i in list:
	#Si ya existe en el diccionario, se suma uno al valor. En caso contrario, se añade con valor uno
	if i in dic:
		dic[i] = dic[i] + 1
	else:
		dic[i] = 1

#Imprimo por pantalla el diccionario
print(dic)