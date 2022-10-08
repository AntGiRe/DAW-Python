max = int(input("Introduce un numero maximo: "))
primos = [2]

for n in range(2,max+1):
  for j in primos:
    if n % j == 0:
      break
    elif((n//j) < j):
      primos.append(n)
      break

print(primos)