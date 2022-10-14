def useFunctionWList(listaNumeros, funcion):
  listaResultado = []
  for i in listaNumeros:
    listaResultado.append(funcion(i))
  return listaResultado

def plusTen(x):
  return (x + 10)

print(useFunctionWList([1,2,3,4], plusTen));