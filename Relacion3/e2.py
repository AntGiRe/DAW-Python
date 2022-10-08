nombre = input("Cual es tu nombre: ")
nota = int(input("Introduce la nota: "))

# if nota in range(0,5) || if nota in range (5,7) -- El segundo numero pilla el anterior

if (nota >= 9):
  print("Tienes sobresaliente")
elif (nota >= 7):
  print("Tienes notable")
elif (nota >= 5):
  print("Estas aprobado")
else:
  print("Estas suspenso")