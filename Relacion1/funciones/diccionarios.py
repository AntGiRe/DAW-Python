dic = {'marca':'opel', 'modelo':'astra'}
print(dic['marca'])
print(dic.keys())

misAlumnos = {
  "alumno1": {
    "nombre":"nombre",
    "edad":23
  },
  "alumno2": {
    "nombre":"nom",
    "edad":24
  }
}

print(misAlumnos["alumno1"])
cumples = {}
while True:
  nombre = input("introduce tu nombre")
  if nombre == "":
    break
  if nombre in cumples:
    print(cumples[nombre], "es el cumpleaños de:", nombre)
  else:
    cumple = input("Cuando es tu cumpleaños")
    cumples[nombre] = cumple
    print("Se ha introducido el cumpleaños de", nombre)