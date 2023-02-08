#Antonio Gil :D
"""Funcion que recibe una frase y la devuelve al reves pero palabra por palabra"""
def espejo(frase):
	if len(frase) > 0:
		return frase.split(" ")[-1] + " " + espejo(frase[:-len(frase.split(" ")[-1])-1])
	else:
		return ""


print(espejo("Hola que tal"))