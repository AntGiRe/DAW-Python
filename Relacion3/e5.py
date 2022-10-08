dni = int(input("Introduce el DNI sin letra: "))

letras = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]

dnifinal = str(dni) + letras[dni%23]
print(dnifinal)