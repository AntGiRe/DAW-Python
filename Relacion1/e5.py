print("Introduzca su peso en kg")
peso = input()
print("Introduz su estatura en cm")
estatura = input()
imc = round(float(peso) / (float(estatura)/100 * float(estatura)/100), 2)

print("Tu índice de masa corporal es", imc, "donde", imc, "es el índice de masa corporal calculado redondeado con dos decimales")