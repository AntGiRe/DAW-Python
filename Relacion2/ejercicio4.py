from asyncio.windows_events import NULL


nombre = input("Introduce tu nombre: ")
asignaturas = []
asig = NULL

while asig != '':
  asig = input("Introduce una asignatura: ")
  if asig != '':
    asignaturas.append(asig)

print("El alumno " + nombre + " está matriculado en: ", end="")

for asig in asignaturas:
  if asig != asignaturas[-1]:
    print(asig, end=", ")
  else:
    print(asig, end=".")