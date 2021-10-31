from tkinter import *
from tkinter import messagebox
import tkinter

# Se define el frame principal
root = Tk()
root.iconbitmap("../MalagaDVD/python.ico")
root.title("frmPrincipal-nuevoTitulo")

# Se obtiene el acho y el alto de la pantalla del sistema
ancho = root.winfo_screenwidth()
alto = root.winfo_screenheight()

# Creación del Frame donde se van a colocar todos los widgets
frmPrincipal = Frame(root, width=ancho, height=alto)
frmPrincipal.pack()

# Función para centrar ventan


def centrarVentana(ancho, alto):
    ancho_ventana = ancho
    alto_ventana = alto
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
        "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    root.resizable(0, 0)


# Instrucciones para establecer la barra de menu
barraMenu = Menu(root)
root.config(menu=barraMenu)

mnubarClientes = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Clientes", menu=mnubarClientes)
mnubarClientes.add_command(label="Formulario Clientes")

mnubarActores = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Actores", menu=mnubarClientes)
mnubarActores.add_command(label="Formulario Actores")

mnubarProtagonistas = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Protagonistas", menu=mnubarClientes)
mnubarProtagonistas.add_command(label="Formulario Protagonistas")

mnubarDirectores = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Directores", menu=mnubarClientes)
mnubarDirectores.add_command(label="Formulario Directores")

mnubarEjemplares = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ejemplares", menu=mnubarClientes)
mnubarEjemplares.add_command(label="Formulario Ejemplares")

centrarVentana(ancho-10, alto-10)

root.mainloop()
