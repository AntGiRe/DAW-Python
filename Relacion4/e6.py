def aplicarFuncion(listaNumeros, funcion):
  listaResultado = []
  for i in listaNumeros:
    listaResultado.append(funcion(i))
  return listaResultado;

def sumaDiez(x):
  return (x + 10)

print(aplicarFuncion([1,2,3,4], sumaDiez));