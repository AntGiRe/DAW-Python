def suma(a, b = 1):
  return a + b

print(suma(3))

def division(a, b):
  try:
    res = a/b
    return res
  except ZeroDivisionError:
    print("El divisor no puede ser cero")

print(division(3,0))

class persona:
  def __init__(self, nombre):
    self.edad = 0
    self.nombre = nombre
  def crece(self,a):
    self.edad += a
  def getNombre(self):
    print("Tu nombre es", self.nombre)

p = persona("Antonio")
p.getNombre()