import re
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysqlconn
from mysql.connector.errors import ProgrammingError

# Se define el frame principal
root = Tk()
root.iconbitmap("../MalagaDVD/imagenes/python.ico")
root.title("frmPrincipal")
root.columnconfigure(2, weight=1)

# Se obtiene el acho y el alto de la pantalla del sistema
ancho = root.winfo_screenwidth()
alto = root.winfo_screenheight()

# Creación del Frame donde se van a colocar todos los widgets
frmPrincipal = Frame(root, width=ancho, height=alto)
frmPrincipal.grid()

# SE define la clase principal


class principal():
    # Función para centrar ventana

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

# Creacion de los Botones CRUD
frmBotones = Frame(frmPrincipal)
frmBotones.configure(bg="light blue")
frmBotones.pack(padx=10, pady=10)

btnClientes = Button(frmBotones, text="Clientes", width=12, height=5)
btnClientes.grid(column=0, row=0, padx=20, pady=20)

btnActores = Button(frmBotones, text="Actores", width=12, height=5)
btnActores.grid(column=0, row=1, padx=20, pady=20)

btnProtagonistas = Button(frmBotones, text="Protagonistas", width=12, height=5)
btnProtagonistas.grid(column=0, row=2, padx=20, pady=20)

btnDirectores = Button(frmBotones, text="Directores", width=12, height=5)
btnDirectores.grid(column=0, row=3, padx=20, pady=20)

btnEjemplares = Button(frmBotones, text="Ejemplares", width=12, height=5)
btnEjemplares.grid(column=0, row=4, padx=20, pady=20)

btnInformes = Button(frmBotones, text="Informes", width=12, height=5)
btnInformes.grid(column=0, row=5, padx=20, pady=20)

principal.centrarVentana(ancho, alto)

root.mainloop()
