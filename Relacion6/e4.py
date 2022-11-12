"""Antonio J Gil 	-	11/11"""
import sys

listOfImg = [];

try:
	with open(sys.argv[1]) as f:
		for linea in f:
			listOfImg.append(linea);
	file = open("index.html", "w")
	file.write("<!DOCTYPE html><html lang='es'><head><title>Imagenes</title><style>img{width:40%}</style></head><body><h1>IMAGENES</h1>");
	for img in listOfImg:
		file.write("<h2>Imagen " + str(listOfImg.index(img)+1) + "</h2>")
		file.write("<img src='" + img + "' alt='Imagen " + str(listOfImg.index(img)+1) + "'>");
	file.write("<p>Imagenes de Freepik.com</p></body>");
	file.close();
except IndexError:
	print("No has dado ningún argumento.");