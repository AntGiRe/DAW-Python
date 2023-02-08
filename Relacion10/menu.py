from tkinter import *
from tkinter import filedialog as FileDialog
from tkinter import messagebox

"""Antonio J. Gil Reyes - 29/01/23"""

# Configuration of the root window
root = Tk()
root.iconbitmap('pencil.ico')
root.title("Bienvenido a mi editor de texto")
root.geometry("650x350")

# Creation of a menu bar
menubar = Menu(root)
root.config(menu=menubar)

# Creation of the widget Text
text = Text(root)

# Function that creates a new file
def new():
	text.pack(expand=True, fill=BOTH)
	root.title("Editando el fichero: Sin título")
	filemenu.entryconfig("Guardar", state="normal")
	filemenu.entryconfig("Cerrar", state="normal")

# Function that saves the file
def saveFile():
	fichero = FileDialog.asksaveasfile(
		initialdir="C:",
		mode='w',
		title = "Guardar un fichero.",
		filetypes=(("Ficheros de texto", "*.txt"),("Todos los ficheros","*.*")),
		defaultextension=".txt"
	)

	AskQuestion = messagebox.askquestion("Salir", "¿Desea guardar el archivo?", icon='warning')
	
	if fichero is not None and AskQuestion == 'yes':
		# Obtenemos el texto del widget Text
		texto2save = text.get(1.0, END)
		fichero.write(texto2save)
		fichero.close()
		root.title("Editando el fichero: " + fichero.name[fichero.name.rfind('/') + 1:])

# Function that opens a file
def openFile():
	fichero = FileDialog.askopenfilename(
		initialdir="C:", 
		filetypes=(
			("Ficheros de texto", "*.txt"),
	    	("Todos los ficheros","*.*")
		), 
		title = "Abrir un fichero."
	)
	print(fichero)

	if fichero is not None:
		root.title("Editando el fichero: " + fichero[fichero.rfind('/') + 1:])
		filemenu.entryconfig("Guardar", state="normal")
		filemenu.entryconfig("Cerrar", state="normal")
		text.pack(expand=True, fill=BOTH)
		text.delete(1.0, END)
		f = open(fichero, "r")
		text.insert("insert", f.read())
		f.close()

# Function that closes the file
def cerrar():
	AskQuestion = messagebox.askquestion("Salir", "¿Desea cerrar el archivo?", icon='warning')
	if AskQuestion == 'yes':
		text.pack_forget()
		text.delete(1.0, END)
		root.title("Bienvenido a mi editor de texto")
		filemenu.entryconfig("Guardar", state="disabled")
		filemenu.entryconfig("Cerrar", state="disabled")

# Creation of the menu
filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Nuevo", command=new)
filemenu.add_command(label="Abrir", command=openFile)
filemenu.add_command(label="Guardar", command=saveFile, state="disabled")
filemenu.add_command(label="Cerrar", state="disabled", command=cerrar)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

menubar.add_cascade(label="Archivo", menu=filemenu)

# Main loop
root.mainloop()