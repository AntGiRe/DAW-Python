"""Antonio Jesús Gil Reyes - Ejercicio 1"""
#Se piden los valores al usuario. Se realiza la multiplicación, sabiendo los menores y mayores.
x1, x2, y1, y2 = int(input("Introduce x1: ")), int(input("Introduce x2: ")), int(input("Introduce y1: ")), int(input("Introduce y2: "))
print ("El area es: " + str((max(x1, x2) - min(x1, x2)) * (max(y1, y2) - min(y1, y2))))