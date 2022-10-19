def decToBin(n):
  res = []
  while (int(n) > 0):
    res.insert(0, str(n%2))
    n //=2
  return int(''.join(res))

def binToDec(n): 
  res = 0
  count = 0
  for n in str(n)[::-1]:
    if (n == "1"):
      res += pow(2, count)
    count += 1
  return res

print(binToDec(11010))
print(decToBin(10))
