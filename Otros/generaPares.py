def generaPares(max):
	i = 2
	while i <= max:
		if i%2 == 0:
			yield i
		i = i + 1

misPares = generaPares(10)

for i in misPares:
    print(i)