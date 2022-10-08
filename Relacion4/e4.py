def translate(text, dic):
  f = text.split()
  for n in f:
    if n in dic:
      print (dic[n], end=" ")
    else:
      print (n, end=" ")  

dic = {}
while True :
  es = input("Introduce una palabra en español (Vacio fin del diccionario): ")
  if es == "":
    break
  en = input("Introduce una palabra en ingles: ")
  dic[es] = en

text = input("Introduce una frase: ")

translate(text, dic)
